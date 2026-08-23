# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="retriv",
    version="0.2.3",
    author="Elias Bassani",
    author_email="elias.bssn@gmail.com",
    description="retriv: A Python Search Engine for Humans.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmenRa/retriv",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "nltk",
        "numba>=0.54.1",
        "tqdm",
        "optuna",
        "unidecode",
        "scikit-learn",
        "ranx",
        "indxr",
        "oneliner_utils",
        "torch",
        "torchvision",
        "torchaudio",
        "transformers[torch]",
        "faiss-cpu",
        "multipipe",
    ],
    extras_require={
        # C++ extension with no prebuilt wheels; needs a build toolchain.
        "krovetz": ["krovetzstemmer"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: General",
    ],
    keywords=[
        "information retrieval",
        "search engine",
        "bm25",
        "numba",
        "sparse retrieval",
        "dense retrieval",
        "hybrid retrieval",
        "neural information retrieval",
    ],
    python_requires=">=3.8",
)
