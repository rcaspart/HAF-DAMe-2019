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

* Implement the advancing of the board with time <!-- .element: class="fragment" -->
	* <!-- .element: class="fragment" --> `advance` function in `gksolite.plain`
* <!-- .element: class="fragment" --> Follow the gitflow workflow for your development

--


# Hints

* Use a feature branch for implementation
	* Don't forget about `--no-ff` when merging
* Make use of a `develop` branch
* <!-- .element: class="fragment" --> The `board` provides a function for determining the number of neighbours for a cell
