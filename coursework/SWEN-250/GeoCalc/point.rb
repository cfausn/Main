# Class of objects representing simple 2D (x,y) points.
# Points are "immutable" - there is no way to assign
# new values to either the x or y coordinates.

class Point

  # The following methods are private.
  private

  # Set the instance variable coordinates for a new Point
  # * The default coordinates are the origin.
  # * This is a private method so it can't be called to change the
  #   coordinates.
  # * We assume that x and y, if provided, can be converted
  #   to floating point.
  #
  def initialize(x = 0.0, y = 0.0)
    @x = x.to_f
    @y = y.to_f
    self
  end

  # The following methods are public.
  public

  # Allow read access to the x and y coordinates via
  # p.x and p.y (for a Point object p).
  attr_reader :x, :y

  # The default string representation of a Point.
  def to_s
    "(#{@x},#{@y})"
  end
end
