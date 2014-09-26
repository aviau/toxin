import wsme
import wsme.types as wtypes


class helloMessage(wtypes.Base):
    message = wsme.wsattr(wtypes.text, mandatory=True)
    """This is the actual message"""

    @classmethod
    def sample(cls):
        return cls(
            message="Hello guys!",
        )
