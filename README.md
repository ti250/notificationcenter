# NotificationCenter

This package implements a class similar to NSNotificationCenter, a variant of the Observer design pattern, from Objective-C and Swift in Python. To install, (soon you will be able to) just use 

	pip install notificationcenter

It consists of one singleton class, NotificationCenter, that is used to add observers and to post notifications. To add an observer, you need to do the following:

```python
from NotificationCenter import *

# Get the NotifiationCenter
notificationcenter = NotificationCenter()
# Define the function you want to perform when you get the notification.
# It should have parameters of (sender, notification name, notification info)
# And return nothing (It can, but it will be thrown away)
def foo(sender, notification_name, info):
	# Do something
# Add an observer
observer = notificationcenter.add_observer(with_block=foo,
										  for_name="bar")
```

Now, if we post a notification to the NotificationCenter with the name "bar", as follows, the above function foo will be executed.

```python
notificationcenter = NotificationCenter()
notificationcenter.post_notification(sender=None,
									with_name="bar")
```

When you are no longer using the observer, you should remove it from the NotificationCenter so that the block is no longer executed. It is done as follows:

```python
notificationcenter.remove_oberver(observer)
```

Detailed documentation is shown below, and the source code is commented.

## API Reference

### add\_observer(with\_block, for\_name, for\_sender=None)

Adds an observer to listen for certain types of notifications.

#### Parameters:

* with\_block: Some function that takes arguments of a sender (any object), notification name (string), and notification info (any object). Any values with\_block returns will be ignored.
	* The function that will be executed when a notification with this name/sender is observed

* for\_name: String
	* The name of the notification for which the observer is registered.

* for\_sender: Any object
	* If this is set, then only notifications from this object are recieved. Else, any notifications with the correct name will be recieved.

#### Returns:

* tuple (String, Any Object, Some Function)
	* This is a tuple of (for\_name, for\_sender, with\_block). It is not meant to be used directly except in the remove\_observer method.

### remove\_observer(observer)

Removes the given observer from the list of active obserers.

#### Parameters:

* observer: tuple (String, Any Object, Some Function)
	* This is the tuple that is returned by add\_observer.

### post\_notification(sender, with\_name, with\_info=None)

Posts a notification with a given name and (optionally) some additional information.

#### Parameters:

* sender: Any Object
	* The sender of this notification

* with\_name: String
	* The name of the notification

* with\_info: Any Object
	* Any additional information for the notification
