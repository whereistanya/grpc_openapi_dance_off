openapi: "3.0.0"


info:
  version: 1.0.0
  title: Jellybean Robot
  description: Jellybean loving robot

servers:
  - url: 'http://localhost:8080'
    description: The server where the robot lives

paths:
  /give:
    post:
      description: Give the robot some beans
      requestBody:
        required: true
        content:
          application/json:
            schema:
             $ref: "#/components/schemas/Jellybeans"
      responses:
        "200":
          description: reply from the robot
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Reply"

components:
  schemas:
    Jellybeans:
      type: object
      required:
      - count
      properties:
        count:
          type: integer
          description: how many beans
        message:
          type: string
          description: A message for the robot.
    Reply:
      type: object
      required:
      - total
      properties:
        total:
          type: integer
          description: How many jellybeans the robot has.
        message:
          type: string
          description: How the robot feels.

# Mistakes I made:
# oh my god, yaml indentation
