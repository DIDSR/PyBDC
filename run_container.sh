# !/bin/bash
# Script to download the container and run PyBDC.
# Assumption: the system is Unix based system and Apptainer (https://apptainer.org) is installed.

# Clone PyBDC container from HuggingFace
git clone https://huggingface.co/didsr/PyBDC-Container

cd PyBDC-Container

read -r -p "Are you providing PyBDC an incident spectrum? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY]) 
        echo "Provide the parent directory path for the incident spectrum file: "
        read directory_path
        echo "Provided path: $directory_path"
        echo "You can access the content of the provided directory in /mnt directory from PyBDC GUI"
        apptainer run --bind $directory_path:/mnt ./PyBDC_container/PyBDC_container.sif
        ;;
    *)
        echo "Incident spectrum files can be accessed from /usr/local/bin/PyBDC/incident_spectrum/"
        apptainer run ./PyBDC_container/PyBDC_container.sif
        ;;
esac
