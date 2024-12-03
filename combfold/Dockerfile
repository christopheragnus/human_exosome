# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set environment variables to non-interactive for installing packages
ENV DEBIAN_FRONTEND=noninteractive

# Install required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    gcc \
    g++ \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    python3 \
    python3-pip \
    git \
    libboost-all-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone the Combfold repository from GitHub
RUN git clone https://github.com/dina-lab3D/CombFold.git opt/combfold

# Change working directory
WORKDIR opt/combfold/CombinatorialAssembler

# Install Combfold
RUN make

# Add Combfold to PATH
ENV PATH="/opt/combfold:$PATH"

# Set the entry point to Combfold (adjust this based on how Combfold is run)
ENTRYPOINT ["combfold"]

# Optionally, you can add a default command or arguments
CMD ["--help"]

