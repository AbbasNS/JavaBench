@file:Suppress("SpellCheckingInspection")

import proguard.gradle.ProGuardTask
import java.time.Duration

plugins {
    java
    application
    checkstyle
}

group = "assignment"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

application {
    mainClass.set("assignment.Sokoban")
}

buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("com.guardsquare:proguard-gradle:7.2.2")
    }
}

tasks.test {
    timeout.set(Duration.ofMinutes(1))
}

dependencies {
    compileOnly("org.jetbrains:annotations:23.0.0")
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.9.0")
    testImplementation("org.junit.jupiter:junit-jupiter-params:5.9.0")
    testImplementation("org.mockito:mockito-core:4.7.0")
    testImplementation("org.mockito:mockito-junit-jupiter:4.7.0")
    testImplementation("org.junit.platform:junit-platform-launcher:1.9.0")
    testImplementation("org.junit.jupiter:junit-jupiter-engine:5.9.0")
}

checkstyle {
    toolVersion = "10.3.2"
    sourceSets = setOf(project.sourceSets.main.get())
}

tasks {
    withType<JavaCompile> {
        // options.compilerArgs = listOf("--enable-preview")
        options.encoding = "UTF-8"
    }
    withType<JavaExec> {
        standardInput = System.`in`
        // jvmArgs("--enable-preview")
    }
    withType<Jar> {
        manifest {
            attributes.apply {
                this["Main-Class"] = application.mainClass.get()
            }
        }
    }
    withType<JacocoReport> {
        dependsOn(test)

        reports {
            xml.required.set(false)
            csv.required.set(false)
            html.outputLocation.set(layout.buildDirectory.dir("jacocoHtml"))
        }
    }
    withType<Test> {
        group = "verification"

        useJUnitPlatform()

        systemProperties(
            "junit.jupiter.execution.timeout.testable.method.default" to "2000 ms"
        )

        // jvmArgs("--enable-preview")
    }

    register<JavaExec>("grade") {
        group = "verification"

        systemProperties(
            "junit.jupiter.execution.timeout.testable.method.default" to "2000 ms"
        )

        dependsOn(testClasses)
        classpath = sourceSets.test.get().runtimeClasspath
        main = "assignment.utils.Grader"
        // jvmArgs("--enable-preview")
    }


    withType<Checkstyle> {

    }

    create<ProGuardTask>("proguard") {
        injars(jar.flatMap { it.archiveFile })
        outjars(jar.flatMap { it.destinationDirectory.file("${project.name}-proguard.jar") })

        libraryjars("${System.getProperty("java.home")}/jmods")
        libraryjars(sourceSets.main.map {
            (it.compileClasspath + it.runtimeClasspath).distinct() - jar.flatMap { jar -> jar.archiveFile }.get().asFile
        })

        keep("public class assignment.Sokoban { public static void main(java.lang.String[]); }")

        optimizations("!class/merging/horizontal")

        printmapping(jar.flatMap { it.destinationDirectory.file("${project.name}-proguard-mapping.txt") })
        overloadaggressively()
        flattenpackagehierarchy()
        allowaccessmodification()
        mergeinterfacesaggressively()
        dontskipnonpubliclibraryclassmembers()
        useuniqueclassmembernames()
        optimizationpasses(5)
    }

    withType<AbstractTestTask> {
        afterSuite(KotlinClosure2({ desc: TestDescriptor, result: TestResult ->
            if (desc.parent == null) { // will match the outermost suite
                println("Results: ${result.resultType} (${result.testCount} tests, ${result.successfulTestCount} successes, ${result.failedTestCount} failures, ${result.skippedTestCount} skipped)")
            }
        }))
    }
}
