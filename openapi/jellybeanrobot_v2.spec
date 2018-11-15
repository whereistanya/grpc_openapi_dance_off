swagger: "2.0"

info:
  version: 1.0.0
  title: Jellybean Robot
  description: Jellybean loving robot

host: localhost:8080
basePath: /v2

paths:
  /users:
    get:
      summary: Returns a list of users.
      description: Optional extended description in Markdown.
      produces:
        - application/json
      responses:
        200:
          description: OK

  /give:
    post:
      description: Give the robot some beans
      operationId: giveBeans
      produces:
        - application/json
      parameters:
      - name: give
        in: body
        description: new beans for the robot
        schema:
          $ref: '#/definitions/Jellybeans'
      responses:
        200:
         description: got beans


definitions:
  Jellybeans:
    type: object
    properties:
      count:
        type: integer
        description: How many beans
      message:
        type: string
        description: A message for the robot

# Mistakes I made:
# not putting colons after the variables
# indentation
# client: https://github.com/kubernetes-client/python/issues/558
# you can't specify a server at runtime? Are you shitting me?
# Had to edit configuration.py and edit "self.host"
# Capitalisation of basePath
# indentation, indentation, so angry

