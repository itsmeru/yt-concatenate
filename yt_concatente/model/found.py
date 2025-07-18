class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):
        return f'<Found(yt={str(self.yt)})>'

    def __repr__(self):
        content = ' : '.join([
            f'yt={str(self.yt)}',
            f'caption={str(self.caption)}',
            f'time={str(self.time)}'
        ])
        return f'<Found( {content} )>'
