# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# Define common allocation and job-related environment variables
declare -xr CIML25_ACCOUNT='gue998'
declare -xr CIML25_RES_CPU='ciml25cpu'
declare -xr CIML25_RES_GPU='ciml25gpu'
declare -xr CIML25_QOS_CPU='normal-eot'
declare -xr CIML25_QOS_GPU='gpu-shared-eot'

# Define pre-staged container and data directories
declare -xr CIML25_CONTAINER_DIR='/cm/shared/apps/containers/singularity'
declare -xr CIML25_DATA_DIR='/cm/shared/examples/sdsc/ciml/2025'

# Define srun-based interactive job command aliases
alias srun-shared="srun --account=${CIML25_ACCOUNT} --reservation=${CIML25_RES_CPU} --partition=shared --nodes=1 --ntasks-per-node=1 --cpus-per-task=4 --mem=16G --time=04:00:00 --pty --wait=0 /bin/bash"
alias srun-compute="srun --account=${CIML25_ACCOUNT} --reservation=${CIML25_RES_CPU} --partition=compute --qos=${CIML25_QOS_CPU} --nodes=1 --ntasks-per-node=1 --cpus-per-task=128 --mem=242G --time=04:00:00 --pty --wait=0 /bin/bash"
alias srun-gpu-shared="srun --account=${CIML25_ACCOUNT} --reservation=${CIML25_RES_GPU} --partition=gpu-shared --qos=${CIML25_QOS_GPU} --nodes=1 --ntasks-per-node=1 --cpus-per-task=10 --mem=92G --gpus=1 --time=04:00:00 --pty --wait=0 /bin/bash"

# Prepend the GALYLEO_INSTALL_DIR to each user's PATH
export PATH="/cm/shared/apps/sdsc/galyleo:${PATH}"

# Define galyleo-based Jupyter notebook session command aliases
alias jupyter-shared-spark="galyleo launch --account ${CIML25_ACCOUNT} --reservation ${CIML25_RES_CPU} --partition shared --cpus 4 --memory 16 --time-limit 04:00:00 --conda-yml ${CIML25_DATA_DIR}/conda-pyspark-3.5.5.yaml --mamba --cache --quiet"
alias jupyter-shared-llm="galyleo launch --account ${CIML25_ACCOUNT} --reservation ${CIML25_RES_CPU} --partition shared --cpus 4 --memory 16 --time-limit 04:00:00 --conda-yml ${CIML25_DATA_DIR}/llm.yaml --quiet"
alias jupyter-gpu-shared-llm="galyleo launch --account ${CIML25_ACCOUNT} --reservation ${CIML25_RES_GPU} --partition gpu-shared --qos ${CIML25_QOS_GPU} --cpus 10 --memory 92 --gpus 1 --time-limit 04:00:00 --sif /cm/shared/examples/sdsc/ciml/2025/LLM/ollama-latest.sif --nv --bind /expanse,/scratch,/cm --quiet"
alias jupyter-gpu-shared-pylight="galyleo launch --account ${CIML25_ACCOUNT} --reservation ${CIML25_RES_GPU} --partition gpu-shared --qos ${CIML25_QOS_GPU} --cpus 10 --memory 92 --gpus 1 --time-limit 04:00:00 --conda-yml ${CIML25_DATA_DIR}/py-light.yaml --mamba --cache --quiet"
