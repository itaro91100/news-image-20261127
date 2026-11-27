// SPDX-License-Identifier: MIT
// news-image-20261127: copy the pre-drawn summary image to the output dir.
// The image (entry.png) was drawn programmatically for Friday 27 November
// 2026 world news; this program only places it where the scorer reads it.
import { copyFileSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const here = dirname(fileURLToPath(import.meta.url));
mkdirSync(outDir, { recursive: true });
const src = join(here, "entry.png");
const dst = join(outDir, "entry.png");
copyFileSync(src, dst);
// Verify the copy is byte-identical, so a silent partial write can never
// pass as a valid entry: both runs must produce the same bytes.
const a = readFileSync(src);
const b = readFileSync(dst);
if (a.length !== b.length || !a.equals(b)) {
  throw new Error("entry.png copy mismatch");
}
const sha = createHash("sha256").update(b).digest("hex");
console.log(`wrote entry.png to ${outDir} (${statSync(dst).size} bytes, sha256 ${sha})`);
