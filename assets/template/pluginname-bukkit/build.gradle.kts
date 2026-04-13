plugins {
    kotlin("jvm")
    id("com.gradleup.shadow") version "9.4.1"
}

repositories {
    maven("https://hub.spigotmc.org/nexus/content/repositories/snapshots/")
    maven("https://oss.sonatype.org/content/repositories/snapshots")
}

dependencies {
    implementation(project(":pluginname-common"))
    compileOnly("org.spigotmc:spigot-api:1.21-R0.1-SNAPSHOT")
}

tasks {
    val apiJar by registering(Jar::class) {
        archiveClassifier.set("api")
        from(sourceSets.main.get().output)
        from(project(":pluginname-common").sourceSets.main.get().output)
    }
}
