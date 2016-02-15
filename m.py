from flask import Flask, request
import os, sys

os.system('mkdir /tmp/tOoLs')
tools = Flask(__name__)

@tools.route("/")
def python():
        if "run" in request.args.keys():
                src=request.args["run"]
                try:
                        src=src.encode('utf8')
                except:
                        pass
                name="n%s"%str(hash(src))
                inp=open('/tmp/tOoLs/%s.m'%name,'w')
                inp.write(src)
                inp.close()
                os.system("rm /tmp/tOoLs/%s.out"%name)
                os.system("touch /tmp/tOoLs/%s.out"%name)
                try:
                        os.system("MathKernel -script /tmp/tOoLs/%s.m </dev/null 1>>/tmp/tOoLs/%s.out 2>>/tmp/tOoLs/%s.out"%(name,name,name))
                except Exception,e:
                        return e.__repr__()
                file=open("/tmp/tOoLs/%s.out"%name,"r")
                ans=file.read()
                file.close()
                return ans
        else:
                return ""

if __name__=="__main__":
        tools.run("0.0.0.0",80,debug=False)

