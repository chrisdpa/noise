HubotSlack = require 'hubot-slack'

module.exports = (robot) ->
  robot.listeners.push new HubotSlack.SlackBotListener robot, /Fail/, (msg) ->
    robot.http("http://brighty.local/noise/on").get() (err, res, body) ->
      msg.send "oh :poop:"

  robot.respond /Fail/, (msg) ->
    robot.http("http://brighty.local/noise/on").get() (err, res, body) ->
      msg.send "oh :poop:"

  robot.respond /:yfronts:/, (msg) ->
    robot.http("http://brighty.local/noise/off").get() (err, res, body) ->
      msg.send ":chicken:"

  robot.listeners.push new HubotSlack.SlackBotListener robot, /normal/, (msg) ->
    robot.http("http://brighty.local/noise/off").get() (err, res, body) ->
      msg.send ":toilet:"
