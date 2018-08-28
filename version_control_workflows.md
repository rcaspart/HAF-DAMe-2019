## Improving your daily workflow

Larger projects usually require more complex workflows than the centralised workflow to manage simultaneous code changes e.g. for different features

* Gitlabflow Workflow <!-- .element: class="fragment" -->
* Forking Workflow <!-- .element: class="fragment" -->
* Gitflow Workflow <!-- .element: class="fragment" -->

--

### Centralised Workflow

* You are working on your own local copy of a central repository
* Your commits are stored locally
* At some point in time you publish your changes to the central repository


	$ git push origin master

--

#### Managing Conflicts

* Before you can publish new features, the updated central commits need to be fetched to rebase your changes on top


	$ git pull --rebase origin master

* This sometimes requires to resolve merge conflicts manually

![Diverged commits from central repository](resources/version_control_diverged.png)

--

#### Managing Conflicts (2)

	CONFLICT (content): Merge conflict in <some-file>

* `git` pauses rebasing until you resolve the merge conflicts
* When you are happy with the results, continue the rebasing


	$ git add <resolved file>
	$ git rebase --continue


* Otherwise, you can still abort and you are back where you started


	$ git rebase --abort


--

### Feature Branch Workflow

* Each feature lives in a dedicated branch


	$ git checkout -b <feature> master

* Encapsulation enables developers to work on a particular feature without interfering with main codebase
* Master branch is spared from broken code
* Leveraging of pull requests

--

#### Merging a feature branch

	$ git checkout master
	$ git pull
	# the actual merge of the new feature
	$ git pull origin <feature>
	# pushing it back to origin
	$ git push

--

### "Gitlabflow" Workflow

![Working with feature branches](resources/version_control_feature.png)

--

### "Gitlabflow" Workflow (2)

* Strict branching model around the concept of a project release
* Robust framework for management of larger projects
* Master branch as main branch
* Features are developed in dedicated branches and merged in the master
* Dedicated branches for deployment of projects

--

#### Finishing a feature branch

	# a new branch is merged into develop
	$ git checkout develop
	# create a new commit to retain historical infos
	$ git merge --no-ff <feature>
	# delete the branch after merging
	$ git branch -d <feature>
	$ git push origin develop

--

### Forking Workflow

* Distributed workflow
* Not a single server-side repository but one server-side repository for each developer
* Project maintainer can push contents of developer repositories to central repository

--

### What works for us

* Combination from Gitlab and Forking Workflow
    * For larger groups it is easier and more flexible to use forks
* Inclusion of `feature` branches
* No further release or hotfix branches

--

## The Pull Request Workflow

* You create a feature in a dedicated branch in your repository
* You push your finalised branch into a public repository
* You file a pull request
* The team reviews the code, discusses it and eventually files change requests
* The repository maintainer merges the feature into the official repository and closes the pull request

--

## Take-away Messages

* Commit often
* Try not to mix up different things into one commit, make up logical units
* Think about your commit messages
	* Include references to tickets if available


	$ git commit -m "$(curl -sL https://bit.ly/funny-mesg | sh)"

* Branching is cheap
