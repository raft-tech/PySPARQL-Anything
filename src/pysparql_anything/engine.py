"""
@author Marco Ratta
@version 25/01/2023
"""

import jnius_config
from pysparql_anything.config import get_path2jar

# Launches JVM

try:
    jnius_config.set_classpath(get_path2jar())  # JVM configuration
    from jnius import autoclass, JavaException  # Launch JVM
except ValueError:
    print('Cannot construct two JVMs. \n'
          + 'Please exit and restart the Python environment and '
          + 'create a new VM for the  CLI.')
    raise
except JavaException:  # Handles JVM exception for an incorrect path
    print('JVM exception occured: \n'
          + 'Check the jar has been dowloaded succesfully:\n'
          + 'try cli.config.has_jar() for a diagnostic value. \n'
          + 'Python environment must be exited and restarted \n'
          + 'for a new JVM to be launched.')
    raise


class Engine:
    """
    The class engine wraps the Java SPARQL Anything Main class.
    Acts as the receiver of the Command pattern.
    """

    def __init__(self):
        """ Constructor for the class Engine. """
        self.reflection = autoclass('com.github.sparqlanything.cli.SPARQLAnything')

    def main(self, args):
        """ Wrapper for the SPARQL Anything main method. """
        self.reflection.main(args)

    def call_main(self, args):
        """ Wrapper for the SPARQL Anything callMain method. """
        return self.reflection.callMain(args)
