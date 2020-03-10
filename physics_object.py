class PhysicsObject:
  def __init__(self, x_pos, y_pos, x_velocity, y_velocity, x_acceleration, y_acceleration, bounce):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.x_velocity = x_velocity
    self.y_velocity = y_velocity
    self.x_acceleration = x_acceleration
    self.y_acceleration = y_acceleration
    self.bounce = bounce
    self.color = 1
    self.gravity = -10

  def update(self, dt, constraints):
    # update velocity
    self.x_velocity += self.x_acceleration*dt
    self.y_velocity += self.y_acceleration*dt

    if abs(self.x_velocity) < 0.1:
      self.x_velocity = 0
    
    if abs(self.y_velocity) < 0.1:
      self.y_velocity = 0

    # apply gravity
    if not(self.y_pos == constraints[3]):
      self.y_velocity += self.gravity*dt

    # calculate the next position
    next_x = self.x_pos + self.x_velocity*dt
    next_y = self.y_pos + self.y_velocity*dt

    # handle boundries (constraints)
    # 0 -> x min
    if next_x < constraints[0]:
      next_x = constraints[0]
      self.x_velocity = self.x_velocity*-0.75
      self.color = (self.color + 1) % 5
    # 1 -> x max
    elif next_x > constraints[1]:
      next_x = constraints[1]
      self.x_velocity = self.x_velocity*-0.75
      self.color = (self.color + 1) % 5

    # 2 -> y min
    if next_y < constraints[2]:
      next_y = constraints[2]
      self.y_velocity = self.y_velocity*-0.75
      self.color = (self.color + 1) % 5
    # 3 -> y max
    elif next_y > constraints[3]:
      next_y = constraints[3]
      self.y_velocity = self.y_velocity*-0.75
      self.color = (self.color + 1) % 5

    if constraints[3] - next_y < 0.01:
      next_y = constraints[3]

    self.x_pos = next_x
    self.y_pos = next_y

  