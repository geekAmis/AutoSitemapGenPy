from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r',encoding='utf-8') as f:
    return f.read()


setup(
  name='AutoSitemapGenPy',
  version='0.0.1',
  author='GeekAmis',
  author_email='gik.lavrov.86@gmail.com',
  description='Automated sitemap generation in xml format for your site files',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/geekAmis/AutoSitemapGenPy',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='sitemap xml ',
  project_urls={
    'GitHub': 'https://github.com/geekAmis'
  },
  python_requires='>=3.5'
)