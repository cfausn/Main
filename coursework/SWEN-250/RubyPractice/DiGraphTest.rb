require './DiGraph_Solution'
require 'test/unit'

class DiGraphTest < Test::Unit::TestCase

  # Create a new graph for the next test

  def setup
    @myGraph = DiGraph.new
  end

  # Is a new graph empty?
  # Does it have size zero?

  def test_for_empty_graph
    assert( @myGraph.empty?, "New graph not empty")
    # ... size test here ...
    assert( @myGraph.numVertices == 0, "Number of vertices > 0" )
  end

  def test_add_vertex
    @myGraph.addVertex("A")
    assert( @myGraph.vertex?("A"), "Vertex not added to graph" )
  end

  def test_out_degree
    @myGraph.addVertex("A")
    assert( @myGraph.outDegree("A") == 0, "Out degree not zero" )
    @myGraph.addEdge("A", "B")
    assert( @myGraph.outDegree("A") == 1, "Out degree not one" )
 end

  def test_add_edge
    @myGraph.addEdge("A", "B")
    assert( @myGraph.edge?("A", "B"), "No edge between vertices" )
  end

  def test_in_degree
   @myGraph.addVertex("A")
   assert( @myGraph.inDegree("A") == 0, "Invalid indegree number")
   @myGraph.addEdge("B", "A")
   @myGraph.addEdge("C", "A")
   assert( @myGraph.inDegree("A") == 2, "Invalid indegree number" )
  end

end
