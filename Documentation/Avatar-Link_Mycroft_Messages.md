# Mycroft Message Bus 

This table shows Mycroft's messages to the hardware enclosure indicating which should be used by Avatar-Link.

✔	Will be integrated into Avatar-Link

?	May be integrated into Avatar-Link at some point

| Use  | Mycroft msg                       | Avatar-Link msg | Description                        |
| ---- | --------------------------------- | --------------- | ---------------------------------- |
| ✔    | enclosure.reset                   | reset           | Restore Default States             |
|      | enclosure.system.mute             |                 | mute speaker                       |
|      | enclosure.system.unmute           |                 | unmute speaker                     |
|      | enclosure.system.blink            |                 | blink a number of times            |
|      | enclosure.eyes.on                 |                 | show eyes                          |
|      | enclosure.eyes.off                |                 | hide eyes                          |
|      | enclosure.eyes.blink              |                 | blink R, L, or both Eyes           |
|      | enclosure.eyes.narrow             |                 | squint                             |
|      | enclosure.eyes.look               |                 | look in one of 5 directions        |
|      | enclosure.eyes.color              |                 | change eye color RGB               |
|      | enclosure.eyes.setpixel           |                 | set individual LED pixels          |
|      | enclosure.eyes.fill               |                 | bar graph / progress bar eyes      |
|      | enclosure.eyes.level              |                 | brightness of eyes                 |
|      | enclosure.eyes.reset              |                 | restore default eyes               |
|      | enclosure.eyes.spin               |                 | roll eyes once                     |
|      | enclosure.eyes.timedspin          |                 | roll eyes (timed)                  |
|      | enclosure.eyes.volume             |                 | eyes indicate speaker volume       |
|      | enclosure.mouth.reset             |                 | restore default mouth              |
| ✔    | enclosure.mouth.talk              | speak_nosync    | for non-synced 'talking' animation |
| ✔    | enclosure.mouth.think             | think           | show thinking                      |
| ✔    | enclosure.mouth.smile             | smile           | show smiling                       |
| ✔    | enclosure.mouth.viseme_list       | viseme.x        | mouth movement per sound (phoneme) |
| ?    | enclosure.mouth.text              | text            | show text                          |
|      | enclosure.mouth.display           |                 | show image from text string        |
| ?    | enclosure.mouth.display_image     | image           | show image from PNG                |
| ?    | enclosure.weather.display         | weather         | show weather info                  |
| ✔    | enclosure.mouth.events.activate   | speak_begin     | enable mouth movement with speech  |
| ✔    | enclosure.mouth.events.deactivate | speak_end       | disable mouth movement with speech |

Table contains all Mycroft Messages emitted through the [Enclosure API](https://github.com/MycroftAI/mycroft-core/blob/dev/mycroft/enclosure/api.py) as of 2019-07-17