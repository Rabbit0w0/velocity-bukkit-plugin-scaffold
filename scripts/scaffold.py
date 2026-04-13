import os
import shutil
import sys
import argparse

def copy_recursive(src, dest):
    if os.path.isdir(src):
        if not os.path.exists(dest):
            os.makedirs(dest)
        for item in os.listdir(src):
            copy_recursive(os.path.join(src, item), os.path.join(dest, item))
    else:
        shutil.copy2(src, dest)

def get_all_files(dir_path):
    all_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def move_package_folders(base_path, old_pkg, new_pkg):
    old_parts = old_pkg.split('.')
    new_parts = new_pkg.split('.')
    old_full_path = os.path.join(base_path, *old_parts)
    
    if os.path.exists(old_full_path):
        new_full_path = os.path.join(base_path, *new_parts)
        os.makedirs(new_full_path, exist_ok=True)
        
        # Move all contents to new location
        for item in os.listdir(old_full_path):
            shutil.move(os.path.join(old_full_path, item), os.path.join(new_full_path, item))
            
        # Cleanup old empty directories
        curr = old_full_path
        for _ in range(len(old_parts)):
            if os.path.exists(curr) and not os.listdir(curr):
                os.rmdir(curr)
                curr = os.path.dirname(curr)
            else:
                break

def main():
    parser = argparse.ArgumentParser(description='Minecraft Plugin Scaffolder')
    parser.add_argument('--project-name', default='MyPlugin', help='Name of the project (CamelCase)')
    parser.add_argument('--package', default='com.example.plugin', help='Base package name')
    parser.add_argument('--output-dir', help='Output directory')
    args = parser.parse_args()

    project_name = args.project_name
    package_name = args.package
    project_slug = project_name.lower()
    
    output_dir = args.output_dir or f"./{project_slug}"
    template_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'template')

    if not os.path.exists(template_dir):
        print(f"Failure: Template directory not found at {template_dir}", file=sys.stderr)
        sys.exit(1)

    try:
        print(f"Scaffolding {project_name} into {output_dir}...")
        
        # Template defaults (after transformation)
        old_slug = "pluginname"
        old_name = "PluginName"
        old_package = "com.example.plugin"

        # Copy everything
        copy_recursive(template_dir, output_dir)

        # Replace content in text files
        all_files = get_all_files(output_dir)
        for file_path in all_files:
            try:
                # Skip binary files
                if file_path.endswith('.jar'):
                    continue
                    
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content.replace(old_package, package_name)
                new_content = new_content.replace(old_name, project_name)
                new_content = new_content.replace(old_slug, project_slug)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                # Rename the main class file if it matches old_name
                if os.path.basename(file_path) == f"{old_name}.kt":
                    new_file_path = os.path.join(os.path.dirname(file_path), f"{project_name}.kt")
                    os.rename(file_path, new_file_path)

            except Exception as e:
                # Silently skip files that aren't UTF-8 (like binary icons/jars)
                pass

        # Rename module folders
        modules = ['bukkit', 'velocity', 'common']
        for mod in modules:
            old_mod_dir = os.path.join(output_dir, f"{old_slug}-{mod}")
            new_mod_dir = os.path.join(output_dir, f"{project_slug}-{mod}")
            if os.path.exists(old_mod_dir):
                os.rename(old_mod_dir, new_mod_dir)

        # Fix package folders
        for mod in modules:
            mod_dir = f"{project_slug}-{mod}"
            for src_type in ["kotlin", "templates"]:
                src_base = os.path.join(output_dir, mod_dir, "src", "main", src_type)
                if os.path.exists(src_base):
                    move_package_folders(src_base, old_package, package_name)

        print(f"Success: Scaffolded {project_name} in {output_dir}")
    except Exception as e:
        print(f"Failure: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
