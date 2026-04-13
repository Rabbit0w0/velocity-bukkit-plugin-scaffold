import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.jetbrains.kotlin.gradle.dsl.KotlinJvmProjectExtension
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "2.3.20" apply false
    kotlin("kapt") version "2.3.20" apply false
    id("org.jetbrains.gradle.plugin.idea-ext") version "1.1.8" apply false
    id("xyz.jpenilla.run-velocity") version "2.3.1" apply false
    id("io.papermc.paperweight.userdev") version "1.7.1" apply false
}

tasks.register<TestReport>("testReport") {
    group = "verification"
    description = "Generates a consolidated test report for all subprojects."
    destinationDirectory.set(layout.buildDirectory.dir("reports/all-tests"))

    // Collect all Test tasks from all subprojects
    val testTasks = subprojects.flatMap { it.tasks.withType<Test>() }
    testResults.from(testTasks.map { it.binaryResultsDirectory })
}

allprojects {
    group = "com.example"
    version = "1.0-SNAPSHOT"

    repositories {
        mavenCentral()
        maven("https://repo.papermc.io/repository/maven-public/")
        maven("https://oss.sonatype.org/content/repositories/snapshots")
    }
}

subprojects {
    apply(plugin = "org.jetbrains.kotlin.jvm")

    val targetJavaVersion = 21
    configure<KotlinJvmProjectExtension> {
        jvmToolchain(targetJavaVersion)
    }

    tasks.withType<KotlinCompile> {
        compilerOptions {
            jvmTarget.set(JvmTarget.fromTarget(targetJavaVersion.toString()))
        }
    }

    dependencies {
        add("testImplementation", "org.junit.jupiter:junit-jupiter:5.14.3")
        add("testImplementation", "org.mockito.kotlin:mockito-kotlin:5.4.0")
        add("testRuntimeOnly", "org.junit.platform:junit-platform-launcher")
    }

    tasks.withType<Test> {
        useJUnitPlatform()
        finalizedBy(rootProject.tasks.named("testReport"))
    }
}
