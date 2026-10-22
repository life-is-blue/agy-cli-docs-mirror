# Choose your Antigravity

Antigravity delivers native agentic assistance across purpose-built product surfaces, with dynamic reasoning controls, multi-agent orchestration, and enterprise-grade security. Evolved from the Agent Manager into a standalone desktop command center (Antigravity App) alongside native terminal, editor, and programmatic SDK interfaces, Antigravity supports both synchronous interactive pair-programming and asynchronous background agent workflows independent of a single IDE. Select any surface below to explore live interface previews, core workflows, and quickstart paths:

Surfaces

v2.5+

Antigravity AppDesktop application

agy · v1.2+

Antigravity CLITerminal client

5 IDEs

For IDEsEditor extensions

Python

Antigravity SDKProgrammatic runtime

New Conversation

Conversation History

Scheduled Tasks

Projects

checkout-service

Discount Code Validationnow

Stripe Webhook Handler2h

inventory-api

Low Stock Alerts1d

web-storefront

Order Summary Drawer

Settings

checkout-service/Discount Code Validation

Add promo code validation and expired coupon checks to the checkout endpoint.

Worked for 11s

I updated `checkout-service` to validate discount codes before creating a payment intent:

*   **PromoValidator**: Check expiration dates and minimum order totals.
*   **CheckoutController**: Return `400 Bad Request` with a clear message for expired codes.

Shall I run the checkout test suite to verify?

Ask anything, @ to mention, / for actions

Gemini 3.8 FlashMedium

Model

Gemini 4 Argon _High_Gemini 3.8 Flash _Medium_Claude Sonnet 5.5 _Thinking_Claude Opus 5.5 _Thinking_GPT-OSS 120B _Medium_

TerminalsProject

`dev@workstation checkout-service % npm test`

PASS src/discounts.test.ts (14 tests)

✓ rejects expired promo codes (9ms)

Standalone Terminals

Conversations

Discount Code Validation

zsh

Artifacts2 files

Implementation Plan

Promo code validation & unit tests

Verification Report

Checkout test suite results

Proposed Changes

\+ if (promo.isExpired()) return res.status(400);

\+ const discount = applyPromo(cart.subtotal, promo);

Browserlocalhost:3000

http://localhost:3000/checkout/preview

Checkout API · Order Summary

FieldValue

Status200 OK

Promo CodeSPRING20 (-$24.00)

Order Total$96.00

A standalone desktop application for launching, orchestrating, and inspecting autonomous agent teams with visual diff and plan inspection.

[Get started with Antigravity App](/docs/getting-started/)[Desktop features guide](/docs/features/)

Antigravity CLI

Antigravity CLI 1.2.14

developer@example.com (Google AI Pro)

Gemini 3.8 Flash (High)

~/projects/checkout-service

\>Run the test suite and fix the failing discount rounding test

▸Thought for 2s, 114 tokens

Running unit tests to reproduce the rounding failure

Bash(npm test -- src/discounts.test.ts)(ctrl+o to expand)

▸Thought for 3s, 142 tokens

Updating currency rounding in calculateDiscount

Edit(src/pricing/discounts.ts)(ctrl+o to expand)

\>

? for shortcutsGemini 3.8 Flash · high

A keyboard-first terminal client that runs Antigravity workflows in local shells, remote cloud environments, and SSH sessions.

[Get started with Antigravity CLI](/docs/getting-started?tab=cli)[CLI reference manual](/docs/cli/reference/)

spring-petclinic

ANTIGRAVITYVS Code

spring-petclinic / Project Analysis And Reporting

Please review this project. Investigate how it works and build a report showing important files and data flows.

*   `BaseEntity`, `NamedEntity`, and `Person` serve as base classes.
*   `Owner`, `Pet`, `Visit`, `Vet`, `Specialty`, and `PetType` define business models.

Key System Controllers:

*   `OwnerController`: Manages owner creation, lookup, and pagination.
*   `PetController`: Handles pet updates/creation using `PetValidator`.
*   `VetController`: Provides HTML vet list and cached JSON endpoint.

Project ReviewComprehensive review report for Spring PetClinic application detailing architecture...

Ask anything, @ to mention, / for actions

Gemini 3.8 Flash Medium

Model

Gemini 4 Argon HighGemini 3.8 Flash MediumClaude Sonnet 5.5 (Thinking)Claude Opus 5.5 (Thinking)GPT-OSS 120B (Medium)

Preview README.mdproject\_review.md

Project ReviewReview ▾

Spring PetClinic - Architectural Review & Technical Analysis

This document provides an architecture review and technical investigation of the **Spring PetClinic** application (`spring-projects/spring-petclinic`).

1\. Project Overview & Tech Stack

Spring PetClinic is a reference application built to showcase modern **Spring Boot** patterns, clean domain-driven architecture, and Java best practices.

*   **Framework:** Spring Boot 4.1.0, Spring MVC, Spring Data JPA, Spring Cache
*   **Java Toolchain:** Java 17 (`build.gradle`)
*   **Database & Persistence:** In-memory H2, MySQL, PostgreSQL

2\. Core Domain Model & Entity Hierarchy

The domain model follows standard Object-Relational Mapping (ORM) principles with common base class inheritance.

README.mdMarkdown Preview

Spring PetClinic Sample Application

Built with Spring Boot, Spring MVC, Thymeleaf, and Spring Data JPA (`spring-projects/spring-petclinic`).

Running PetClinic Locally

Clone the repository and start the embedded server using the Maven or Gradle wrapper:

*   **Maven:** `./mvnw spring-boot:run`
*   **Gradle:** `./gradlew bootRun`
*   **Local Endpoint:** `http://localhost:8080`

Database Configuration

Uses an in-memory **H2** database by default, with Docker Compose profiles for `mysql` and `postgres`.

main⊗ 0 ⚠ 2 ⓘ 1Java: Ready

Gradle: Build Error

Editor extensions that embed agentic capabilities, inline completions, and side-panel interactions directly in your IDE.

[Get started with IDE extensions](/docs/getting-started?tab=ide)[Supported extensions guide](/docs/ide/extensions/)

agent\_pipeline.pyPython 3.10+

```python
from google.antigravity import Agent, LocalAgentConfig
from google.antigravity.hooks.policy import allow, deny

# Configure stateful agent harness and safety policies
config = LocalAgentConfig(
    policies=[allow("view_file"), deny("run_command")],
    system_instructions="You are a senior software architect.",
)

# Execute multi-turn conversation in async context
async with Agent(config) as agent:
    response = await agent.chat("Audit the repository architecture.")
    print(await response.text())
```

A programmatic Python SDK for building, customizing, and deploying autonomous AI agents and harnesses in your own applications and CI/CD pipelines.

[Get started with Antigravity SDK](/docs/getting-started?tab=sdk)[Tools and skills API](/docs/sdk/tools/)

* * *

## Core agent capabilities

Every Antigravity surface runs on a shared, highly optimized agent harness co-trained with Gemini models, combining synchronous turn-by-turn code editing and tool execution with asynchronous background subagents, scheduled cron sidecars, and automated verification loops:

Frontier Gemini models

Gemini 4 & 3.8

Co-trained with Google DeepMind. Powering all local agents with frontier speed, configurable reasoning levels, and large context capacity across Gemini 4 Argon, Gemini 3.8 Flash, and Gemini 3.1 Pro.

[Model specifications](/docs/models/)

Asynchronous subagents

Parallel execution

Delegate complex background tasks to concurrent subagents working across isolated Git worktrees without blocking your active terminal or editor session.

[Subagents guide](/docs/subagents/)

Visual artifacts

Verification loops

Track and verify agent output with structured visual reports, including interactive implementation plans, unified multi-file diffs, and browser session recordings.

[Artifact inspection](/docs/artifacts/)

Security by design

Bounded access

Enforce local execution safeguards with granular tool approval gates, workspace directory scoping, local proxying, and corporate VPC Service Controls.

[Permissions and security](/docs/permissions/)

Google platform integrations

Curated bundles of skills, MCP servers, and extensions engineered with product teams across Google—including Firebase, Android, Modern Web, Chrome DevTools, Flutter, Google Cloud Data, Maps, Science, and the Antigravity SDK.

[View all bundles](/docs/build-with-google/)

* * *

## Frontier models and dynamic reasoning

Antigravity leverages Google DeepMind’s frontier Gemini models with dynamic reasoning controls. Adjust reasoning effort per conversation turn or delegate long-running tasks to autonomous agent swarms:

### Interactive model and thinking level selector

Experience the model selector directly below. Antigravity lets you adjust reasoning depth and model speed dynamically per conversation turn.

[Model specs and limits](/docs/models/)

* * *

## Product comparison

Compare primary capabilities and execution environments across Antigravity surfaces:

AllCore workflowExtensibilitySecurity & enterprise

| Capability | 
App

 | 

CLI

 | 

IDE Ext.

 | 

SDK

 |
| --- | --- | --- | --- | --- |
| Desktop application |  |  |  |  |
| Terminal user interface (TUI) |  |  |  |  |
| [Editor extensions (VS Code, JetBrains, VS, Zed, Xcode)](/docs/ide/extensions/) |  |  |  |  |
| [Programmatic Python SDK](/docs/sdk/overview/) |  |  |  |  |
| [Remote control & headless execution](/docs/remote-control/) |  |  |  |  |
| [Workspace & Git worktree isolation](/docs/projects/) |  |  |  |  |
| [Multi-agent swarms (/teamwork-preview)](/docs/teamwork/) |  |  |  |  |
| [Deep reasoning mode (/boost)](/docs/boost/) |  |  |  |  |
| [Interactive visual artifacts & diffs](/docs/artifacts/) |  |  |  |  |
| [Sandboxed Chromium browser automation](/docs/ide/browser/) |  |  |  |  |
| [Custom skills (SKILL.md) & rule files](/docs/skills/) |  |  |  |  |
| [Model Context Protocol (MCP) clients](/docs/mcp/) |  |  |  |  |
| [Scheduled tasks & cron sidecars](/docs/sidecars/) |  |  |  |  |
| [Corporate SSO & BYOID (Workforce Identity)](/docs/enterprise/) |  |  |  |  |
| [Regional data residency (US & EU)](/docs/enterprise/) |  |  |  |  |
| [VPC Service Controls (VPC-SC)](/docs/enterprise/) |  |  |  |  |
| [Request, response & telemetry logging](/docs/enterprise/) |  |  |  |  |

Capabilities are tailored to each surface's execution target. Enterprise features under IDE Ext. apply to Antigravity IDE extensions (GA in VS Code & Visual Studio; Preview in JetBrains, Zed, and Xcode).

[Features guide](/docs/features/)

* * *

## User and enterprise tiers

Antigravity supports individual developers and enterprise engineering organizations with Google Cloud security, regional data residency, and VPC Service Controls:

Deployment tiers

IndividualEnterprise suitev2.5+

Individual developers

Designed for software engineers, researchers, and open-source contributors who need frontier autonomous coding assistance on their local workstation.

Free tier · Pro & Ultra plans

Desktop & terminal clients

Full access to the native Antigravity App desktop application and the high-speed `agy` command-line interface.

All IDE extensions

Integration with VS Code, JetBrains IDEs, Xcode, Zed, and Visual Studio with dedicated agent panels, interactive plans, and inline diff reviews.

Flexible individual plans & AI credits

Start at $0/month on the Free plan, or upgrade to Google AI Plus, Pro, or Ultra for higher rate limits and optional AI credit overages.

Skills, MCP & rules

Author project-level custom skills (`SKILL.md`), connect stdio/SSE MCP servers, and define behavior rule sets.

[Get started free](/docs/getting-started/)[View AI credits & plans](/docs/plans/)

Enterprise engineering organizations

Engineered for organizations requiring Google Cloud governance, regional data residency, VPC Service Controls, and enterprise identity management.

Google Cloud ToS · VPC-SC

[

Corporate SSO & BYOIDGoogle Cloud & WIF

Authenticate with Google Cloud SSO, Bring Your Own Identity (BYOID) via Workforce Identity Federation (such as Okta), or Application Default Credentials.



](/docs/enterprise/)[

Regional data residencyUS, EU & Global

Control where model inference and data processing occur across global, US multi-region, and European Union multi-region endpoints.



](/docs/enterprise/)[

VPC Service ControlsGoogle Cloud

Enforce network service perimeters and private connectivity with Google Cloud VPC Service Controls (VPC-SC) and IAM role governance.



](/docs/enterprise/)[

Request & telemetry loggingCloud Audit

Configure project telemetry and full request and response logging directly within your Google Cloud project for security and compliance.



](/docs/enterprise/)[

Flexible enterprise billingLicenses or Pay-as-you-go

Choose consumption-based billing via the Gemini Enterprise Agent Platform API or Gemini Enterprise licenses with included quotas and managed overages.



](/docs/enterprise/)[

Zero model training guaranteeData privacy

Governed by the Google Cloud Terms of Service. Your prompts, code, and transcripts are never stored outside your private environments or used to train models.



](/docs/enterprise/)

[Explore enterprise suite](/docs/enterprise/)[Architecture & case studies](/use-cases/enterprise/)

* * *

## Documentation pillars

Explore the documentation across six core architectural pillars:

[

Start Here

Get Started

Install the Antigravity App, set up the CLI, integrate the SDK, and configure IDE extensions.

](/docs/getting-started/)[

Concepts

Learn

Master foundational concepts including Workspaces, Git Worktrees, and Sessions.

](/docs/features/)[

Extensibility

Extend

Author custom Skills (`SKILL.md`), connect MCP Servers, and define Lifecycle Hooks.

](/docs/skills/)[

Security

Enterprise

Corporate SSO & BYOID, Regional Data Residency, VPC Service Controls, and Cloud Logging.

](/docs/enterprise/)[

Ecosystem

Build with Google

Firebase, Chrome DevTools, Android CLI, Dart & Flutter, Science, and Data Agent Kit skills.

](/docs/build-with-google/)[

Specs

Reference

CLI command manuals, models specifications, settings schemas, and API references.

](/docs/cli/reference/)