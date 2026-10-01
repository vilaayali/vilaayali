<a id="top"></a>

<a href="https://www.vilaayali.com"><img src="./assets/repo-card.svg" width="100%" alt="vilaayali/vilaayali — Full-stack developer building real-time web apps, clean APIs and fast UIs." /></a>

<div align="center">

### 🔗 [vilaayali.com](https://www.vilaayali.com)

[![website](https://img.shields.io/badge/website-vilaayali.com-f78166?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.vilaayali.com)
[![linkedin](https://img.shields.io/badge/LinkedIn-connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/syedvilaayali)
[![email](https://img.shields.io/badge/email-say_hi-30363d?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vilaayali89@gmail.com)

[![build](https://img.shields.io/badge/build-passing-3fb950?style=flat-square&logo=githubactions&logoColor=white)](#)
[![version](https://img.shields.io/badge/release-v2026.10-1f6feb?style=flat-square&logo=github&logoColor=white)](#%EF%B8%8F-releases)
[![react](https://img.shields.io/badge/React-20232a?style=flat-square&logo=react&logoColor=61DAFB)](#-dependencies)
[![next](https://img.shields.io/badge/Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white)](#-dependencies)
[![node](https://img.shields.io/badge/Node.js-1b2a1b?style=flat-square&logo=nodedotjs&logoColor=5FA04E)](#-dependencies)
[![license](https://img.shields.io/badge/license-MIT-6e7681?style=flat-square)](#-license)
[![followers](https://img.shields.io/github/followers/vilaayali?style=flat-square&logo=github&label=followers&color=30363d)](https://github.com/vilaayali?tab=followers)
[![stars](https://img.shields.io/github/stars/vilaayali?style=flat-square&logo=github&label=stars&color=e3b341&affiliations=OWNER)](https://github.com/vilaayali?tab=repositories)
![views](https://komarev.com/ghpvc/?username=vilaayali&style=flat-square&color=f78166&label=profile+views)

[**Install**](#-installation) · [**Usage**](#-usage) · [**Projects**](#-projects) · [**Architecture**](#%EF%B8%8F-architecture) · [**Changelog**](#-git-log) · [**Activity**](#-activity) · [**Contributing**](#-contributing) · [**FAQ**](#-faq)

</div>

> [!TIP]
> **Open to collaborations.** Got a project in mind? Jump to [Contributing](#-contributing) — I usually reply within a day.

## 📦 Installation

```bash
git clone https://github.com/vilaayali/vilaayali.git
cd vilaayali && open https://www.vilaayali.com
```

## ✨ Features

```diff
- slow pages, full reloads, undocumented endpoints
+ instant UIs, live updates over WebSockets, APIs with Swagger docs
```

- ⚡ **Real-time** — live data streaming over WebSockets
- 🔐 **APIs** — REST with JWT auth, Zod validation and Swagger docs
- 🎨 **UI** — responsive, lazy-loaded, pixel-tidy
- 🛒 **Commerce** — storefronts and admin panels built to scale

## 🚀 Usage

```ts
import { vilaayali } from "vilaayali";

const app = await vilaayali.build({
  frontend: ["React", "Next.js", "Tailwind", "Redux"],
  backend:  ["Node.js", "Express", "PostgreSQL", "MongoDB"],
  realtime: "Socket.io",
});

app.ship(); // ✔ compiled  ✔ tested  ✔ deployed
```

## 📁 Projects

| | Project | What it does | Built with |
| :-: | :-- | :-- | :-- |
| 🔐 | [**blog-management-api**](https://github.com/vilaayali) | REST API with auth, posts, search & uploads | `Node.js` `Express` `PostgreSQL` |
| 🧭 | [**convers-by-ginkgo**](https://github.com/vilaayali) | Admin panel with routing & validated forms | `React` `Next.js` `MUI` |
| 🛒 | [**sanaullah-store**](https://github.com/vilaayali) | Storefront wired to live product APIs | `Next.js` `Sass` |
| 🌐 | [**vilaayali.com**](https://www.vilaayali.com) · [code](https://github.com/vilaayali/vilaayali_portfolio) | My personal site | `React` `Vite` `Vercel` |

<details>
<summary><b>blog-management-api</b> — more details</summary>

<br>

- JWT authentication with author-owned posts
- Search, filters and pagination
- Image uploads via Cloudinary
- Full Swagger / OpenAPI docs
- `Node.js` · `Express` · `PostgreSQL` · `Sequelize` · `Zod`

</details>

<details>
<summary><b>convers-by-ginkgo</b> — more details</summary>

<br>

- Responsive admin panel with dynamic routing
- Validated forms and a reusable component library
- `React` · `Next.js` · `MUI` · `Sass`

</details>

<details>
<summary><b>sanaullah-store</b> — more details</summary>

<br>

- Storefront integrated with live product and user APIs
- Clean, responsive UI across devices
- `React` · `Next.js` · `MUI` · `Sass`

</details>

## 🏗️ Architecture

How I usually put an app together:

```mermaid
flowchart LR
  U([👤 User]) --> FE["⚛️ Next.js / React<br/>Tailwind · Redux"]
  FE -- REST --> API["🟢 Node.js + Express<br/>JWT · Zod · Swagger"]
  FE <-. "WebSocket" .-> RT["⚡ Socket.io"]
  RT --- API
  API --> DB[("🐘 PostgreSQL<br/>Sequelize")]
  API --> MDB[("🍃 MongoDB<br/>Mongoose")]
  API --> CDN["☁️ Cloudinary"]
  FE --> V["▲ Vercel"]
```

## 🌳 git log

```mermaid
gitGraph
  commit id: "hello world"
  branch frontend
  commit id: "convers-by-ginkgo"
  commit id: "sanaullah-store"
  checkout main
  merge frontend
  branch backend
  commit id: "blog-management-api"
  commit id: "jwt + swagger"
  checkout main
  merge backend
  commit id: "vilaayali.com" type: HIGHLIGHT
  commit id: "next: your idea?"
```

## 🧱 Dependencies

```json
{
  "dependencies": {
    "react": "latest", "next": "latest", "redux": "latest",
    "tailwindcss": "latest", "@tanstack/react-query": "latest",
    "node": "latest", "express": "latest", "socket.io": "latest",
    "postgresql": "latest", "mongodb": "latest"
  },
  "devDependencies": { "coffee": "*", "git": "*", "vercel": "*" }
}
```

## 📊 Activity

> [!NOTE]
> Stats include private repositories.

<img src="https://streak-stats.demolab.com?user=vilaayali&hide_border=true&background=0D1117&stroke=30363D&ring=F78166&fire=F78166&currStreakLabel=F78166&sideLabels=E6EDF3&currStreakNum=E6EDF3&sideNums=E6EDF3&dates=9198A1&border_radius=6" width="49%" /> <img src="./assets/languages.svg" width="49%" />

<img width="100%" alt="all-time contribution graph" src="./assets/contrib.svg" />

<p align="center"><img src="https://komarev.com/ghpvc/?username=vilaayali&style=for-the-badge&color=f78166&label=profile+views" /></p>

<img width="100%" alt="contribution snake" src="./assets/snake.svg" />

## 🏷️ Releases

| Version | Notes |
| :-- | :-- |
| **v2026.10** `latest` | New profile · open to collaborations |
| v2025.08 | Real-time apps over WebSockets |
| v2024.11 | First production e-commerce work |

## 🤝 Contributing

> [!IMPORTANT]
> Ideas, projects and bug reports welcome. Press <kbd>Ctrl</kbd> + <kbd>Enter</kbd> on an [email to me](mailto:vilaayali89@gmail.com), or ping me on [LinkedIn](https://linkedin.com/in/syedvilaayali).

## ❓ FAQ

<details>
<summary><b>Are you open to freelance or contract work?</b></summary>
<br>
Yes — <a href="mailto:vilaayali89@gmail.com">email me</a> with a short brief and timeline.
</details>

<details>
<summary><b>What kind of projects do you enjoy most?</b></summary>
<br>
Real-time apps, dashboards and anything where speed and clean UX matter.
</details>

<details>
<summary><b>Where can I see more of your work?</b></summary>
<br>
On <a href="https://www.vilaayali.com">vilaayali.com</a> and in the pinned repositories below.
</details>

## 📄 License

MIT © Syed Vilaay Ali — free to reach out, fork ideas and build together.

<div align="center">
<br>
<sub>Made with ☕ · ⭐ star a repo if something helped · <a href="#top">back to top ↑</a></sub>
</div>
