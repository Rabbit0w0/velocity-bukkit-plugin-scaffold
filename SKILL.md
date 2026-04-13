---
name: velocity-bukkit-plugin-scaffold
description: Scaffolds a new multi-module Minecraft plugin project for Velocity and Bukkit using Kotlin and Gradle. Use when starting a new cross-platform Minecraft plugin that requires a common module, a Bukkit module, and a Velocity module.
---

# Minecraft Plugin Scaffold

## Overview

This skill provides a complete boilerplate for a Minecraft plugin project that supports both **Velocity** and **Bukkit/Spigot/Paper**. It uses **Kotlin**, **Gradle (Kotlin DSL)**, and includes a **Common** module for shared logic.

## Quick Start

To create a new project using this scaffold:

1.  **Run the scaffolding script**:
    ```bash
    python <path-to-skill>/scripts/scaffold.py --project-name "MyAwesomePlugin" --package "com.example.myplugin" --output-dir "./my-awesome-plugin"
    ```
2.  **Navigate to the new directory**:
    ```bash
    cd ./my-awesome-plugin
    ```
3.  **Build the project**:
    ```bash
    ./gradlew build
    ```

## Project Structure

The generated project follows this structure:

- `[project]-common`: Shared logic, models, and constants.
- `[project]-bukkit`: Bukkit/Spigot/Paper specific implementation.
- `[project]-velocity`: Velocity specific implementation.
- `build.gradle.kts`: Root build script managing dependencies and versions.

## Capabilities

### 1. Multi-Platform Support
Automatically sets up the necessary dependencies for both Velocity and Bukkit APIs.

### 2. Common Module
A shared module is provided to avoid code duplication between platforms.

### 3. Automated Scaffolding
The `scaffold.py` script handles:
- Renaming the project and modules.
- Updating package names in all files.
- Renaming the main class files.
- Correcting folder structures to match the new package.

## Customization

After scaffolding, you can customize:
- `gradle.properties`: Update version and group.
- `build.gradle.kts`: Add more dependencies or change plugin versions.
- `[project]-common/src/main/templates`: Customize generated build constants.
