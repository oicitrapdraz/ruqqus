from flask import *
import time

from ruqqus.classes import *
from ruqqus.__main__ import app, cache


@app.route('/fun/roulette/opt_in', methods=["POST"])
@is_not_banned
def roulette_opt_in(v):

    v.is_enrolled=True
    db.add(v)
    db.commit()

    return '', 204

@app.route('/fun/roulette/opt_out', methods=["POST"])
@is_not_banned
def roulette_opt_in(v):

    v.is_enrolled=False
    db.add(v)
    db.commit()

    return '', 204

@app.route('/fun/roulette', methods=["GET"])
@auth_desired
def fun_roulette(v):

    now=int(time.time())

    count=db.query(User).filter(
        or_(
            User.is_banned==0,
            user.unban_utc<now
            ),
        User.is_enrolled==True
        ).count()

    return render_template("fun/roulette",
        v=v,
        count=count)