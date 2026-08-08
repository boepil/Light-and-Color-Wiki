---
name: fix-github-pages-deployment
description: A cheatsheet for fixing GitHub Pages "Deployment cancelled" or "Multiple artifacts" errors in GitHub Actions.
---

# Fix GitHub Pages Deployment Errors

If the user encounters errors while deploying a Quartz or generic static site to GitHub Pages using the `actions/deploy-pages@v4` workflow, use these guidelines to troubleshoot and fix the issue.

## 1. "Deployment cancelled" Error
**Symptoms:**
- The workflow fails instantly at the `deploy-pages` step with: `Error: Deployment cancelled.`
- The user has already verified that their repository settings (`Settings > Pages > Source`) are correctly set to **"GitHub Actions"**.

**Root Cause:**
This is typically caused by a glitch or strict implicit branch protection rule in GitHub's automatically generated `github-pages` environment for the repository.

**Solution:**
Instruct the user to manually delete the environment so GitHub can recreate it cleanly:
1. Go to the repository on GitHub.
2. Click **Settings** > **Environments** (left sidebar).
3. Find the `github-pages` environment and click the **trash can icon** to delete it.
4. Go back to the **Actions** tab and re-run the workflow. GitHub will recreate the environment and the deploy should succeed.

## 2. "Multiple artifacts named 'github-pages' were unexpectedly found" Error
**Symptoms:**
- The workflow fails at the `deploy-pages` step with: `Error: Multiple artifacts named "github-pages" were unexpectedly found for this workflow run. Artifact count is 2.`

**Root Cause:**
This happens when the user clicks **"Re-run failed jobs"** on a workflow run that has already successfully uploaded a `github-pages` artifact. GitHub attempts to attach a second artifact with the same name to the same run context, causing a collision.

**Solution:**
Do not use "Re-run failed jobs". Instead, trigger a completely fresh workflow run. 
You can do this for the user by pushing an empty commit to the repository:
```bash
git commit --allow-empty -m "Trigger fresh deploy to fix artifact duplication"
git push
```
This forces GitHub Actions to start a brand new run from a clean slate, bypassing the duplicate artifact issue.
