# Add files to staging area
git add .

# Commit changes
git commit -m "Initial commit"

# Create a branch
git branch testing/my-testing
git checkout testing/my-testing

# Make changes # ... edit files ...

# Stage and commit
git add .
git commit -m "Add new testing"

# Push the branch to GitHub
git push origin testing/my-testing

# You can check your current branch anytime with:
git branch

# Switch back to main
git checkout main

# Merge testing branch
git merge testing/my-testing

# Push the merged main to GitHub
git push origin main

---

# Stage changes
git add .

# Commit
git commit -m "Add new Note to Main"

# Push origin main
git push origin main