# Eye in the Sky

The goal of this project is to develop a Telegram Bot which would
allow me to control remotely a camera connected to a Raspberry Pi
in my home. Moreover, the ability to read other sensors connected
to the Pi would also be a useful feature for me.

The bot should reply only to its owner. Usage:
```
$ python eyeinthesky.py <token> <ownerId>
```

A great source of inspiration for this project came from
[home surveillance monitored via telegram](http://ginolhac.github.io/posts/diy-raspberry-monitored-via-telegram/),
kudos to Aurélien Ginolhac for the nice article on this.



## Current Status

The bot is able to reply to a single user with simple text messages.
I want to work on the following features:
* Send pictures from the webcam to the owner
* Plot temperature and humidity vs time with [matplotlib](https://matplotlib.org/)
  and send it to the owner.
