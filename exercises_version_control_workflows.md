# Exercise 4

* The board develops over time
* Neighbours preserve, kill or spawn alive cells


	###		o cell
	#o#		# neighbour
	###

--

# The Cells

* 2 Neighbours: Survive
* 3 Neighbours: Spawn or Survive
* `or die`

--

# Your Mission

* Currently the board uses a default number of neighbours for each cell when advancing <!-- .element: class="fragment" -->
	* <!-- .element: class="fragment" --> Adapt this behaviour to calculate the number of neighbours in the `advance` function in `gksolite.plain`
* <!-- .element: class="fragment" --> Follow the gitflow workflow for your development

--


# Hints

* Use a feature branch for implementation
	* Don't forget about `--no-ff` when merging
* <!-- .element: class="fragment" --> The `board` provides a function for determining the number of neighbours for a cell
