# 2025-01 - Example Streamlit App 1
This provides the example application for using Streamlit to create a rapid PoC of a website with a user area, through combining the use of Pages and Authentication plugin.

This project would not be possible without the excellent [Streamlit Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator/tree/main)

## To get started
### Build
```
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Run
```
streamlit run app.py
```

### Develop
The main application is defined within app.py.

Authentication details are stored within auth.yml

Subpages are under components directory.


## See Also
* [Streamlit Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator/tree/main)
* [Pages & Navigation](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation)


