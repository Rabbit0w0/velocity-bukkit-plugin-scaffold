plugins {
    kotlin("kapt")
    id("com.gradleup.shadow") version "9.4.1"
    id("xyz.jpenilla.run-velocity")
}

repositories {
    maven("https://repo.papermc.io/repository/maven-public/") {
        name = "papermc-repo"
    }
}

dependencies {
    implementation(project(":pluginname-common"))
    compileOnly("com.velocitypowered:velocity-api:3.4.0-SNAPSHOT")
    kapt("com.velocitypowered:velocity-api:3.4.0-SNAPSHOT")
}

tasks {
    runVelocity {
        velocityVersion("3.4.0-SNAPSHOT")
    }

    val apiJar by registering(Jar::class) {
        archiveClassifier.set("api")
        from(sourceSets.main.get().output)
        from(project(":pluginname-common").sourceSets.main.get().output)
    }
}
