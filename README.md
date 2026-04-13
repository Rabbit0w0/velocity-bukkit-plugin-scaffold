# Velocity/Bukkit Plugin Scaffolder Skill

A [Gemini CLI](https://github.com/google-gemini/gemini-cli) skill for scaffolding cross-platform Minecraft plugin projects. It sets up a multi-module Gradle project with Kotlin support, targeting both **Velocity** and **Bukkit/Spigot/Paper**.

## Features

- **Multi-Platform**: Scaffolds modules for Velocity and Bukkit.
- **Common Module**: Includes a shared module for common logic and models.
- **Automated Setup**: Renames packages, classes, and folders based on your project name.
- **Modern Stack**: Uses Kotlin and Gradle (Kotlin DSL).
- **Ready-to-Build**: Includes `plugin.yml` for Bukkit and `@Plugin` annotation for Velocity.

## Structure

- `assets/template`: The source template for the project.
- `scripts/scaffold.py`: The Python script that performs the scaffolding transformation.
- `SKILL.md`: Documentation for the Gemini CLI skill.
- `velocity-bukkit-plugin-scaffold.skill`: The skill definition file.

## Usage

If you have this skill installed in Gemini CLI, you can activate it:

```bash
/activate velocity-bukkit-plugin-scaffold
```

Or run the scaffolding script directly:

```bash
python scripts/scaffold.py --project-name "MyAwesomePlugin" --package "com.example.myplugin" --output-dir "./my-plugin"
```

### Options

- `--project-name`: The name of your plugin (e.g., `MyPlugin`).
- `--package`: The base package name (e.g., `com.example.plugin`).
- `--output-dir`: Where to generate the project.

## Development

To test the scaffolder:

1. Modify `assets/template`.
2. Run `python scripts/scaffold.py --project-name "TestPlugin" --output-dir "./test-output"`.
3. Verify the generated files in `./test-output`.
4. Run `rm -rf test-output` when finished.
