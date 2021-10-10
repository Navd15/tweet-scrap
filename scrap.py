import twint
import sys


temp=[tuple(i.split('=')) for i in sys.argv[1:]]
args=dict(temp)

assert args.get('q') and args.get('since') and args.get('until') , f'query(q), since (yyyy-mm-dd) & unitl (yyyy-mm-dd) are required args'

c = twint.Config()
print(args.get('q'))
c.Search = f"#{args.get('q')}"
c.Custom["tweet"] = ['date','user_id','tweet','id']

with open(f"{args.get('q')}.csv",'w',encoding='utf-8') as f:
    f.write('created_at,user,text,id\n')

c.Output = f"{args.get('q')}.csv"
c.Store_csv=True
c.Since=args.get('q')

c.Since=args.get('since')
c.Until=args.get('until')
twint.run.Search(c)