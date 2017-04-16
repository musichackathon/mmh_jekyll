# Demonstration of Jekyll for Monthly Music Hackathon

Website can be seen at http://musichackathon.github.io/mmh_jekyll

# Making changes

There are a few basic steps that will be common to any website change:

1. Create a branch
2. Make the changes
3. Create a pull request
4. Get comments or feedback from other organizers
5. Make further changes/commits as appropriate
5. Merge the branch

A more detailed description of that process can be found in the 
[Understanding the GitHub Flow Guide](https://guides.github.com/introduction/flow/).

## Changing one file easily

For small changes (such as updating this README.md or updating an event), 
the whole thing can be done on github.com without leaving the browser. 

To create a branch, make changes, and create a pull request:

1. Browse to the file
2. Click the pencil icon to edit the file and make your changes
3. In the 'Commit changes box' add 
[an appropriate title and description](https://github.com/blog/926-shiny-new-commit-styles).
4. *IMPORTANT*: Be sure to select the option "Create a new branch for this commit and start a pull
request."
5. Click "Propose file change".
6. On the next screen, add one or more appropriate reviewers.
7. Click 'Create pull request'.

## To add a new event

The process to add a new event is similar to the process for making a small change and can also
complete be done in the browser.

1. Browse to the _events directory.
2. Open template.md and select and copy the contents.
3. Back in the _events directory, clic, "Create a new file".
4. Paste the template into the new file.
5. Remove the first line of the ["front matter"](https://jekyllrb.com/docs/frontmatter/), the one
that says, "published: false".
6. Update all the other fields and content as needed.
7. Follow the directions from step 3 above to write a description, create a new branch, 
propose changes, add reviewers, and create the pull request.