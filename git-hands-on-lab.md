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
# Switch back to main
git checkout main

# Merge testing branch
git merge testing/my-testing