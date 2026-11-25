# Build a playable 3D browser world

Available on: Antigravity App, Antigravity CLI

Build **Skycrest Archipelago**, a playable low-poly 3D world, from an empty folder using [`/swarm`](/docs/swarm) and [`/browser`](/docs/commands/browser). This build guide draws inspiration from [Google’s Three-Live project](https://github.com/google/three-live) and Three.js builders. One prompt splits terrain, glider physics, crystals, and tests across four parallel agents. You then verify the live WebGL scene visually with no local 3D software required.

Skycrest Archipelago walkthrough: run one /swarm prompt, watch four parallel agents build and test the 3D world, and inspect three sky presets in /browser. The video has sound. Parts of the video are sped up.

Availability and prerequisites

*   **`/swarm` (Preview)**: Available on **all plans** in the **Antigravity App** and **Antigravity CLI** (when admin settings allow it on business and enterprise accounts). Parallel workers use quota faster than a single thread.
*   **`/browser`**: Built-in browser checks require **Antigravity App `v2.30.0+`** (`v2.31.0+` for download prompts) on a personal Google Account. In the **Antigravity CLI** and on business or enterprise accounts, `/browser` uses local **Google Chrome `v144+`**. Turn on `chrome://inspect/#remote-debugging` first (and keep `npx` on your `PATH` in the CLI).

* * *

## Before you start

| Requirement | Details |
| --- | --- |
| **Format** | Single starter prompt + live visual check |
| **Antigravity surface** | [Antigravity App](/download) (`v2.30.0+` for the built-in browser; `v2.31.0+` for download prompts) or Antigravity CLI (`agy`) |
| **Local tools** | Node.js `22+` (for `node --test`, plus `npx` for CLI `/browser`) and Python 3 (to serve static files). Internet access is required for the Three.js CDN module. |
| **Browser backend** | Built-in browser on personal App accounts (`v2.30.0+`). Local Google Chrome `v144+` with `chrome://inspect/#remote-debugging` turned on for CLI and business or enterprise accounts. |
| **MCP or plugins** | None. No Blender, Unity, or external texture packs required. |

## What you’ll practice

*   **[Prompting and instructions](/docs/learn/prompting)**: Scoping goals, file boundaries, constraints, and acceptance checks inside one starter prompt.
*   **[Context windows and tokens](/docs/learn/context-and-tokens)**: Keeping each subsystem in its own clean worker context instead of one oversized thread.
*   **[How AI agents work](/docs/learn/how-agents-work)**: Coordinating parallel named workers and an independent `@verifier` on a shared `/swarm` board.
*   **[Verification and guardrails](/docs/learn/verification-and-guardrails)**: Pairing fast `node --test` math assertions with live `/browser` visual and console checks.

* * *

## Build it step by step

To build and verify Skycrest Archipelago from scratch, do the following:

1.  **Create an empty workspace folder** and open it in the Antigravity App (or run `agy` inside it):
    
    ```bash
    mkdir skycrest-archipelago && cd skycrest-archipelago
    ```
    
2.  **Run the starter prompt.** Make sure `skycrest-archipelago` is your active project first. Click **Try in Antigravity** on the card below, or click **Copy prompt** and paste it into your workspace composer or `agy`:
    
    ```prompt
    /swarm Build a playable 3D explorer ("Skycrest Archipelago") using a Three.js CDN import map in index.html (no bundler or npm install) in four slices: @world (src/terrain_math.js, src/world.js: island, ocean, pines, rocks, 4 sky islands, clouds, Daylight/Golden Sunset/Starlight presets toggled with T), @physics (src/player.js: glider with WASD or arrow-key movement, Space jump/glide, Shift boost, island landings, terrain-clamped Follow and C-key Orbit camera), @gameplay (src/gameplay.js, index.html, src/main.js: 8 glowing crystals, Web Audio chimes, glass HUD, inline SVG favicon), and @verifier (tests/world_math.test.mjs Node tests for terrain, islands, and crystals, plus local server and /browser check of all 3 sky presets with zero console errors).
    ```
    
    | Worker | Owned files | Responsibilities |
    | --- | --- | --- |
    | **`@world`** | `src/terrain_math.js`, `src/world.js` | Procedural archipelago, animated ocean, instanced pines and rocks, 4 floating sky islands, clouds, and three sky presets toggled with `T`. |
    | **`@physics`** | `src/player.js` | Glider-explorer with `WASD` or arrow-key movement, `Space` jump and glide, `Shift` boost, island landings, and Follow plus `C`\-key Orbit camera. |
    | **`@gameplay`** | `src/gameplay.js`, `index.html`, `src/main.js` | Three.js CDN import map, 8 glowing sky crystals, Web Audio chimes, glass HUD, and inline SVG favicon. |
    | **`@verifier`** | `tests/world_math.test.mjs` | Node unit tests for elevation, islands, and crystals, plus local serving and `/browser` verification across all 3 sky presets. |
    
3.  **Follow the parallel agents on the Swarm board.** Watch `@world`, `@physics`, `@gameplay`, and `@verifier` post progress, test runs, and screenshots on the shared board:
    
    **Antigravity App:**
    
    Click **Open the Swarm UI** in the coordinator’s reply to open the **Swarm** side pane. Switch between **Board**, **Members**, and **Graph** to inspect live messages and active workers.
    
    ![The Antigravity App running the Skycrest Archipelago swarm, with the coordinator conversation on the left listing the world, physics, gameplay, verifier, and monitor workers above the Open the Swarm UI link, and the Swarm side pane on the right showing posts 1 through 9 on the Board tab as each worker hands off files to verifier and verifier confirms 12 passing tests and zero browser console errors](/assets/image/docs/learn/build-3d-swarm-board.webp)
    
    **Antigravity CLI:**
    
    Run `/swarm board` or press Alt + S to open the live board full screen. Press Alt + J to jump to pending approvals, or Ctrl + K to approve from the prompt.
    
    ![The Antigravity CLI full-screen Swarm board for Skycrest Archipelago showing the six-member Roster on Gemini 4 Carbon Medium, the Posts feed with coordinator briefs and handoffs from world, physics, gameplay, and verifier, and selected Message 8 where verifier confirms 12 passing unit tests and zero browser console errors across all three sky presets](/assets/image/docs/learn/build-3d-swarm-cli-board.webp)
    
4.  **Run the tests and launch the island locally:**
    
    ```bash
    node --test tests/world_math.test.mjs
    python3 -m http.server 4173
    ```
    
    Open `http://localhost:4173` in your browser and explore:
    
    *   w a s d or ↑ ↓ ← → to move
    *   Space to jump, and hold Space to glide
    *   Shift to boost
    *   t to switch between **Daylight**, **Golden Sunset**, and **Starlight**
    *   c to toggle between **Follow** and **Orbit** cameras
5.  **Run a visual check anytime you edit the scene.** Copy and paste this prompt into your `skycrest-archipelago` conversation (or click **Try in Antigravity** with that project active):
    
    ```prompt
    /browser Open http://localhost:4173, verify zero console errors, cycle through Daylight, Golden Sunset, and Starlight modes with the T key, test WASD and Space gliding, and show screenshots confirming the camera never clips into terrain.
    ```
    

* * *

## Why `/swarm` and `/browser` fit this build

*   **Clear file boundaries prevent collisions.** Terrain math, glider physics, crystal gameplay, and tests each own separate files. `/swarm` runs `@world`, `@physics`, `@gameplay`, and `@verifier` in parallel, while idle workers wait on the board without using tokens.
*   **Unit tests and visual checks catch different bugs.** `node --test` verifies finite heightmap math and crystal placement. `/browser` opens the live WebGL scene, checks console logs, inspects all three sky presets, and confirms clean camera framing.

* * *

## Why this prompt works

Four reusable guardrails are baked into the starter prompt to avoid common 3D web pitfalls:

*   **Three.js CDN import map (`index.html`)**: Avoids bundler setup and avoids `npm install` network prompts inside the terminal sandbox.
*   **Pure math module (`src/terrain_math.js`)**: Lets `@verifier` run fast `node --test` assertions before launching a browser.
*   **Inline SVG favicon (`data:image/svg+xml`)**: Prevents `/favicon.ico` 404 noise during automated `/browser` console checks.
*   **Terrain-clamped camera rules in `@physics`**: Keeps Follow and Orbit cameras above hillsides and trees, verified through `/browser` screenshots.

* * *

## Make it yours

Once your archipelago runs, copy and paste any prompt below into your open `skycrest-archipelago` conversation. You can also click **Try in Antigravity** while that project is active:

### Rainstorm mode (Quick tweak)

```prompt
/swarm Add a toggleable rainstorm mode with falling rain, dark storm waves, and glowing light trails behind the glider when holding Space to glide. Verify with /browser that frame rate stays smooth and console errors stay at zero.
```

### 60-second ring race (Intermediate)

```prompt
/swarm Add 6 floating sky rings linking the four floating islands, a 60-second countdown timer, and a best-time scoreboard in localStorage. Have @verifier add Node unit tests for timer start and reset and verify the HUD stays readable at 390px mobile width with /browser.
```

### Save as a 3D file (Export)

Export your island as a standard 3D model file you can open in other 3D apps:

```prompt
Add a top-right HUD button that downloads the island as a standard 3D model file (.glb) you can open in other 3D apps using Three.js's built-in GLTFExporter (three/addons/exporters/GLTFExporter.js), then verify in /browser that clicking it triggers a clean download with zero console errors.
```

In the Antigravity App built-in browser (`v2.31.0+`), `blob:` file downloads pause once for approval. Click **Yes, allow this time** when prompted.

* * *

## Troubleshooting

*   **Site approval prompt for `localhost:4173`**: Under **Default**, **Auto**, or **Request Review**, `/browser` asks **Allow executing actions on this URL?**. Choose **Yes, allow `localhost:4173` in this conversation**.
*   **Port `4173` is already in use**: `@verifier` may still be serving the folder. Open `http://localhost:4173` directly, or start Python on another port such as `python3 -m http.server 4174`.
*   **CLI or enterprise `/browser` cannot connect**: Open local Google Chrome (`v144+`) and go to `chrome://inspect/#remote-debugging`. Turn on **Allow remote debugging for this browser instance**, then click **Allow** within 60 seconds when prompted.
*   **Alt + S does not open the CLI board on macOS**: Set your terminal to send Option as Alt (Meta). You can also run `/swarm board`, which works in every terminal.

* * *

## Next steps

[

Feature guide

Swarm (/swarm)

Learn how coordinators, named workers, and verifiers coordinate on the shared board.

](/docs/swarm/)[

Verification

Browser use

Explore built-in browser agents, parallel tabs, and Chrome DevTools checks.

](/docs/browser/)[

AI foundations

Prompting and instructions

Review the prompt anatomy and constraint patterns behind this build.

](/docs/learn/prompting/)