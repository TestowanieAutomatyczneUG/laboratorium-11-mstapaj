class Note:
    def __init__(self,name,note):
        if isinstance(name,str):
            self.name=name
        else:
            raise TypeError('Name musi być typu string')
        if isinstance(note,int) and str(note)!='True' and str(note)!='False':
            if 2<=note<=6:
                self.note=note
            else:
                raise ValueError('Note musi być z przedziału 2-6')
        else:
            raise TypeError('Note musi być typu Int')

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note