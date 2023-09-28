# Script to generate a diagram map of the laboratory
# Use:
# python diagram.py <diagram-name>
# python diagram.py diagram

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.os import LinuxGeneral
from diagrams.onprem.ci import Jenkins


diagram_file_name = "diagram" # without .png extension

graph_attr = {
    "labelloc": "t",
    "fontsize": "30",
    "bgcolor": "white",
    #"size": "15,7!",
    #"ratio": "compress"
    }

with Diagram("DevOps Basics",
             outformat="png",
             filename=diagram_file_name,
             show=False,
             direction="LR",
             graph_attr=graph_attr):
    jenkins_url = "http://jenkins.onlylabs.io"

    jenkins = Jenkins(label=f"Jenkins Server \n{jenkins_url}")
    # Users
    user = LinuxGeneral('\n'.join([
    'Developer',
    'Linux Client'
    ]))
    
    user >> jenkins

