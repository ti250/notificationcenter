class NotificationCenter(object):
    """
    Singleton class which handles communication between objects using notifications.
    """
    _instance = None

    def __init__(self):
        # Makes a dictionary of observers if it doesn't already exist.
        # (This should only happen when the first instance is created)
        if not hasattr(self, 'observers'):
            self.observers = {}

    def __new__(cls, *args, **kwargs):
        """
        Makes sure NotificationCenter is a singleton
        """
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def add_observer(self, with_block, for_name, for_sender=None):
        """
        Adds an observer to listen for certain types of notifications.

        Parameters
        ----------
        with_block: Some function that takes arguments of a sender (any object), notification name (string), and notification info (any object).
        Any values with_block returns will be ignored.
            The function that will be executed when a notification with this name/sender is observed

        for_name: String
            The name of the notification for which the observer is registered.

        for_sender: Any object
            If this is set, then only notifications from this object are recieved.
            Else, any notifications with the correct name will be recieved.

        Returns
        -------
        tuple (String, Any Object, Some Function)
            This is a tuple of (for_name, for_sender, with_block).
            It is not meant to be used directly except in the remove_observer method.

        """
        observer = (for_name, for_sender, with_block)
        if for_name not in self.observers:
            self.observers[for_name] = [observer]
        else:
            self.observers[for_name].append(observer)
        return observer

    def remove_observer(self, observer):
        """
        Removes the given observer from the list of active obserers.

        Parameters
        ----------
        observer: tuple (String, Any Object, Some Function)
            This is the tuple that is returned by add_observer.
        """
        obss = self.observers[observer[0]]
        if obss is not None:
            if len(obss) == 1:
                self.observers.pop(observer[0])
            for index, obs in enumerate(obss):
                if obs == observer:
                    del obss[index]
                    break

    def post_notification(self, sender, with_name, with_info=None):
        """
        Posts a notification with a given name and (optionally) some additional information.

        Parameters
        ----------
        sender: Any Object
            The sender of this notification

        with_name: String
            The name of the notification

        with_info: Any Object
            Any additional information for the notification
        """
        if with_name in self.observers:
            obss = self.observers[with_name]
            if obss is not None:
                for observer in obss:
                    if observer[1] is None or observer[1] == sender:
                        observer[2](sender, with_name, with_info)
