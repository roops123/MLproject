# MLproject demo

Commands that have been used:-
a.conda -p venev python -y to create virtual env with python installation along with default option set to yes.
b.conda activate venev/ to activate virtual env.
c.git init 
d.git add README.md
e.git commit -m "message"
f.git branch -M main
g.git remote add origin HTTPS_URL
h.git push -u origin main

Requirements.txt contains the list of packages required for project deploymnent."-e ." has added at the last of requirements.txt to make sure that if in case ,requirements.txt is called by using the command pip install -r requirements.txt ,setup.py will be called automatically.