# Game of Life (2)

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

# Exercise 2

* Implement the advancing of the board with time <!-- .element: class="fragment" -->
	* <!-- .element: class="fragment" --> `advance` function in `gksolite.plain`
* Follow the gitflow workflow for your development

--


# Hints

* Use a feature branch for implementation
	* Don't forget about `--no-ff` when merging
* Make use of a `develop` branch
* The `board` already provides a function for deriving the number of neighbours
