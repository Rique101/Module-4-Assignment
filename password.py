class credential:
    """The credential class includes methods that create a username and password and determine
    the strength of the password.
    """
    def __init__(self, password: str, username: str):
        """Initializes a credential using the specified password and username.
        
        Args:
            password (str): specified password
            username (str): specified username
        
        :ivar __password: password for this credential
        :ivar __username: username for this credential
        
        Raises:
            ValueError: indicates specified password is None
            ValueError: indicates specified username is None
        """
        try:
            if (password is None):
                raise ValueError("Password may not be None")
            elif (username is None):
                raise ValueError("Username may not be None")
        except ValueError as e:
            exit(e)
        finally:
            self.__password = password
            self.__username = username
    def getPassword(self):
        """Returns the password for the calling credential.
        
        Returns:
            str: password
        """
        return self.__password

    def setPassword(self, password: str):
        """Sets the password in the calling credential to the specified password.
        
        Args:
            password (str): specified password
        
        Raises:
            ValueError: indicates specified password is None
        """
        try:
            if (password is None):
                raise ValueError("Password may not be None")
        except ValueError as e:
            exit(e)
        finally:
            self.__password = password

    def getUsername(self):
        """Returns the username for the calling credential.
        
        Returns:
            str: username
        """
        return self.__username

    def setUsername(self, username: str):
        """Sets the username in the calling credential to the specified username.
        
        Args:
            username (str): specified username
        
        Raises:
            ValueError: indicates specified username is None
        """
        try:
            if (username is None):
                raise ValueError("Username may not be None")
        except ValueError as e:
            exit(e)
        finally:
            self.__username = username

    def __strength(self):
        """Determines the strength of the calling credential's password based on its content and length.
        
        Returns:
            str: "Weak" if the password contains only numbers or only characters or
            is fewer than 8 characters in length, else "Strong"
        """
        if self.__password.isdigit() or self.__password.isalpha() or len(self.__password) < 8 or self.__password.isalnum():
            return "Weak"
        else:
            return "Strong"
    def __str__(self):
        """Returns string representation of the calling credential.
        
        Returns:
            str: string representation of the calling credential
        """
        return f"Username: {self.__username} Password: {self.__password} Strength: {self.__strength()}"
    
    def __eq__(self, other):
        """Tests if the calling credential is equal to the specified object.
        
        Args:
            other: the specified object
        
            Returns:
            Boolean: True if the calling credential is equal to the specified 
            object, else False
        """
        if not isinstance(other, credential):
            return False
        return self.__password == other.getPassword() and self.__username == other.getUsername()

