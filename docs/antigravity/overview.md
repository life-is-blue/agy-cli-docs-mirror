# Choose your Antigravity

Antigravity delivers native agentic assistance across purpose-built product surfaces, with dynamic reasoning controls, multi-agent orchestration, and enterprise-grade security. Evolved from the Agent Manager into a standalone desktop command center (Antigravity app) alongside native terminal, editor, and programmatic SDK interfaces, Antigravity supports both synchronous interactive pair-programming and asynchronous background agent workflows independent of a single IDE. Select any surface below to explore live interface previews, core workflows, and quickstart paths:

Surfaces

desktop\_windowsv2.5+

Antigravity appDesktop application

terminalagy · v1.2+

Antigravity CLITerminal client

extension5 IDEs

For IDEsEditor extensions

code\_blocksPython

Antigravity SDKProgrammatic runtime

view\_sidebararrow\_backarrow\_forward

addNew Conversation

historyConversation History

scheduleScheduled Tasks

Projects

filter\_listcreate\_new\_folder

foldercheckout-service

Discount Code Validationnow

Stripe Webhook Handler2h

folderinventory-api

Low Stock Alerts1d

folderweb-storefront

Order Summary Drawer

settingsSettings

checkout-service/Discount Code Validation

more\_vertOpen IDE

Add promo code validation and expired coupon checks to the checkout endpoint.

Worked for 11schevron\_right

I updated `checkout-service` to validate discount codes before creating a payment intent:

*   **PromoValidator**: Check expiration dates and minimum order totals.
*   **CheckoutController**: Return `400 Bad Request` with a clear message for expired codes.

Shall I run the checkout test suite to verify?

content\_copythumb\_upthumb\_down

Ask anything, @ to mention, / for actions

add

Gemini 3.8 FlashHighexpand\_less

Model

Gemini 4 Argon _High_checkGemini 3.8 Flash _High_checkGemini 3.1 Pro _High_checkClaude Sonnet 5.5 _Thinking_checkClaude Opus 5.5 _Thinking_check

micarrow\_forward

terminaldescriptionweb\_asset

addview\_sidebar

TerminalsProjectexpand\_more

addview\_list

`dev@workstation checkout-service % npm test`

PASS src/discounts.test.ts (14 tests)

✓ rejects expired promo codes (9ms)

Standalone Terminals

Conversations

Discount Code Validation

terminalzsh

Artifacts2 files

assignment

Implementation Plan

Promo code validation & unit tests

fact\_check

Verification Report

Checkout test suite results

Proposed Changes

\+ if (promo.isExpired()) return res.status(400);

\+ const discount = applyPromo(cart.subtotal, promo);

Browserlocalhost:3000

globehttp://localhost:3000/checkout/preview

Checkout API · Order Summary

FieldValue

Status200 OK

Promo CodeSPRING20 (-$24.00)

Order Total$96.00

A standalone desktop application for launching, orchestrating, and inspecting autonomous agent teams with visual diff and plan inspection.

[Get started with Antigravity apparrow\_forward](/docs/getting-started/)[Desktop features guide](/docs/features/)

terminalAntigravity CLI

more\_horiz

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

[Get started with Antigravity CLIarrow\_forward](/docs/getting-started?tab=cli)[CLI reference manual](/docs/cli/reference/)

arrow\_backarrow\_forward

folderspring-petclinicexpand\_more

splitscreenview\_sidebar

folder\_copysearchfork\_rightauto\_awesomeextension

settings

ANTIGRAVITYVS Code

spring-petclinic / Project Analysis And Reporting

addmore\_vert

Please review this project. Investigate how it works and build a report showing important files and data flows.

*   `BaseEntity`, `NamedEntity`, and `Person` serve as base classes.
*   `Owner`, `Pet`, `Visit`, `Vet`, `Specialty`, and `PetType` define business models.

Key System Controllers:

*   `OwnerController`: Manages owner creation, lookup, and pagination.
*   `PetController`: Handles pet updates/creation using `PetValidator`.
*   `VetController`: Provides HTML vet list and cached JSON endpoint.

description

Project ReviewComprehensive review report for Spring PetClinic application detailing architecture...

Ask anything, @ to mention, / for actions

add

Gemini 3.8 Flash Highexpand\_less

Model

Gemini 4 Argon HighcheckGemini 3.8 Flash HighcheckGemini 3.1 Pro HighcheckClaude Sonnet 5.5 (Thinking)checkClaude Opus 5.5 (Thinking)check

arrow\_forward

articlePreview README.mddescriptionproject\_review.md

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

fork\_right main⊗ 0 ⚠ 2 ⓘ 1Java: Ready

Gradle: Build Error

Editor extensions that embed agentic capabilities, inline completions, and side-panel interactions directly in your IDE.

[Get started with IDE extensionsarrow\_forward](/docs/getting-started?tab=ide)[Supported extensions guide](/docs/ide/extensions/)

agent\_pipeline.pyPython 3.10+

```
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

[Get started with Antigravity SDKarrow\_forward](/docs/getting-started?tab=sdk)[Tools and skills API](/docs/sdk/tools/)

* * *

## Core agent capabilities

Every Antigravity surface runs on a shared, highly optimized agent harness co-trained with Gemini models, combining synchronous turn-by-turn code editing and tool execution with asynchronous background subagents, scheduled cron sidecars, and automated verification loops:

psychologyFrontier Gemini models

Gemini 4 & 3.8

Co-trained with Google DeepMind. Powering all local agents with frontier speed, configurable reasoning levels, and large context capacity across Gemini 4 Argon, Gemini 3.8 Flash, and Gemini 3.1 Pro.

[Model specificationsarrow\_forward](/docs/models/)

group\_workAsynchronous subagents

Parallel execution

Delegate complex background tasks to concurrent subagents working across isolated Git worktrees without blocking your active terminal or editor session.

[Subagents guidearrow\_forward](/docs/subagents/)

splitscreenVisual artifacts

Verification loops

Track and verify agent output with structured visual reports, including interactive implementation plans, unified multi-file diffs, and browser session recordings.

[Artifact inspectionarrow\_forward](/docs/artifacts/)

shieldSecurity by design

Bounded access

Enforce local execution safeguards with granular tool approval gates, workspace directory scoping, local proxying, and corporate VPC Service Controls.

[Permissions and securityarrow\_forward](/docs/permissions/)

hub

Google platform integrations

Curated bundles of skills, MCP servers, and extensions engineered with product teams across Google—including Firebase, Android, Modern Web, Chrome DevTools, Flutter, Google Cloud Data, Maps, Science, and the Antigravity SDK.

[View all bundlesarrow\_forward](/docs/build-with-google/)

* * *

## Frontier models and dynamic reasoning

Antigravity leverages Google DeepMind’s frontier Gemini models with dynamic reasoning controls. Adjust reasoning effort per conversation turn or delegate long-running tasks to autonomous agent swarms:

psychology

### Interactive model and thinking level selector

Experience the model selector directly below. Antigravity lets you adjust reasoning depth and model speed dynamically per conversation turn.

[Model specs and limitsarrow\_forward](/docs/models/)

* * *

## Product comparison

Compare primary capabilities and execution environments across Antigravity surfaces:

AllCore workflowExtensibilitySecurity & enterprise

| Capability | 
desktop\_windowsApp

 | 

terminalCLI

 | 

extensionIDE Ext.

 | 

code\_blocksSDK

 |
| --- | --- | --- | --- | --- |
| Desktop application | check | close | close | close |
| Terminal user interface (TUI) | close | check | close | close |
| [Editor extensions (VS Code, JetBrains, VS, Zed, Xcode)](/docs/ide/extensions/) | close | close | check | close |
| [Programmatic Python SDK](/docs/sdk/overview/) | close | close | close | check |
| [Remote control & headless execution](/docs/remote-control/) | check | check | close | close |
| [Workspace & Git worktree isolation](/docs/projects/) | check | check | close | check |
| [Multi-agent swarms (/teamwork-preview)](/docs/teamwork/) | check | check | close | close |
| [Deep reasoning mode (/boost)](/docs/boost/) | check | check | close | close |
| [Interactive visual artifacts & diffs](/docs/artifacts/) | check | check | check | close |
| [Sandboxed Chromium browser automation](/docs/ide/browser/) | check | close | close | close |
| [Custom skills (SKILL.md) & rule files](/docs/skills/) | check | check | check | check |
| [Model Context Protocol (MCP) clients](/docs/mcp/) | check | check | check | check |
| [Scheduled tasks & cron sidecars](/docs/sidecars/) | check | check | close | close |
| [Corporate SSO & BYOID (Workforce Identity)](/docs/enterprise/) | check | check | check | check |
| [Regional data residency (US & EU)](/docs/enterprise/) | check | check | check | check |
| [VPC Service Controls (VPC-SC)](/docs/enterprise/) | check | check | check | check |
| [Request, response & telemetry logging](/docs/enterprise/) | check | check | check | check |

infoCapabilities are tailored to each surface's execution target. Enterprise features under IDE Ext. apply to Antigravity IDE extensions (GA in VS Code & Visual Studio; Preview in JetBrains, Zed, and Xcode).

[Features guidearrow\_forward](/docs/features/)

* * *

## User and enterprise tiers

Antigravity supports individual developers and enterprise engineering organizations with Google Cloud security, regional data residency, and VPC Service Controls:

verified\_userDeployment tiers

personIndividualdomainEnterprise suitev2.5+

Individual developers

Designed for software engineers, researchers, and open-source contributors who need frontier autonomous coding assistance on their local workstation.

Free tier · Pro & Ultra plans

desktop\_windows

Desktop & terminal clients

Full access to the native Antigravity app desktop application and the high-speed `agy` command-line interface.

extension

All IDE extensions

Integration with VS Code, JetBrains IDEs, Xcode, Zed, and Visual Studio with dedicated agent panels, interactive plans, and inline diff reviews.

toll

Flexible individual plans & AI credits

Start at $0/month on the Free plan, or upgrade to Google AI Plus, Pro, or Ultra for higher rate limits and optional AI credit overages.

build

Skills, MCP & rules

Author project-level custom skills (`SKILL.md`), connect stdio/SSE MCP servers, and define behavior rule sets.

[Get started freearrow\_forward](/docs/getting-started/)[View AI credits & plans](/docs/plans/)

Enterprise engineering organizations

Engineered for organizations requiring Google Cloud governance, regional data residency, VPC Service Controls, and enterprise identity management.

Google Cloud ToS · VPC-SC

[badge

Corporate SSO & BYOIDGoogle Cloud & WIF

Authenticate with Google Cloud SSO, Bring Your Own Identity (BYOID) via Workforce Identity Federation (such as Okta), or Application Default Credentials.



](/docs/enterprise/)[public

Regional data residencyUS, EU & Global

Control where model inference and data processing occur across global, US multi-region, and European Union multi-region endpoints.



](/docs/enterprise/)[lan

VPC Service ControlsGoogle Cloud

Enforce network service perimeters and private connectivity with Google Cloud VPC Service Controls (VPC-SC) and IAM role governance.



](/docs/enterprise/)[fact\_check

Request & telemetry loggingCloud Audit

Configure project telemetry and full request and response logging directly within your Google Cloud project for security and compliance.



](/docs/enterprise/)[account\_balance\_wallet

Flexible enterprise billingLicenses or Pay-as-you-go

Choose consumption-based billing via the Gemini Enterprise Agent Platform API or Gemini Enterprise licenses with included quotas and managed overages.



](/docs/enterprise/)[shield\_lock

Zero model training guaranteeData privacy

Governed by the Google Cloud Terms of Service. Your prompts, code, and transcripts are never stored outside your private environments or used to train models.



](/docs/enterprise/)

[Explore enterprise suitearrow\_forward](/docs/enterprise/)[Architecture & case studies](/use-cases/enterprise/)

* * *

## Documentation pillars

Explore the documentation across six core architectural pillars:

[

rocket\_launchStart Here

Get Started

Install the Antigravity app, set up the CLI, integrate the SDK, and configure IDE extensions.

](/docs/getting-started/)[

schoolConcepts

Learn

Master foundational concepts including Workspaces, Git Worktrees, and Sessions.

](/docs/features/)[

extensionExtensibility

Extend

Author custom Skills (`SKILL.md`), connect MCP Servers, and define Lifecycle Hooks.

](/docs/skills/)[

domainSecurity

Enterprise

Corporate SSO & BYOID, Regional Data Residency, VPC Service Controls, and Cloud Logging.

](/docs/enterprise/)[

menu\_bookEcosystem

Build with Google

Firebase, Chrome DevTools, Android CLI, Dart & Flutter, Science, and Data Agent Kit skills.

](/docs/build-with-google/)[

auto\_storiesSpecs

Reference

CLI command manuals, models specifications, settings schemas, and API references.

](/docs/cli/reference/)