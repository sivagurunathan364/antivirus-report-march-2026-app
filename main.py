import streamlit as st
import pandas as pd

st.header("ANTIVIRUS REPORT MARCH 2026")
if st.button("press"):
    df=pd.DataFrame({
        "date":["17/03/2026","17/03/2026","17/03/2026","25/03/2026","25/03/2026",
                "25/03/2026","25/03/2026","25/03/2026","25/03/2026"        ],
        "department":["civi engineering tlc2","civil engineering tlc2","civil engineering tlc2",
                      "civil engineering admin office","civil engineering admin office",
                      "civil engineering admin office","civil engineering admin office",
                      "civil engineering admin office","physics department"        ],
        "system name":["Ravindra gettu","sivakumar","sivakumar","arunkumar",
                       "Ravikanth reddy","arunkumar(lisence only)","roslin",
                       "dhinesh (lisence only)","atanu"    ],
        "ip adress":["10.48.58.141","10.42.58.2","none","10.21.6.39","10.21.5.186",
                     "10.21.6.91","10.21.5.196","10.21.6.113","10.42.110.142"        ],
        "time":["11.30am","11.35am","11.45am","12.15pm","12.25pm","12.42pm","12.51pm",
                "12.58pm","03.45pm"

        ]
                                                 
    })
    st.write(df)