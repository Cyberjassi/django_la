from .models import Singer,Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']



class SingerSerializer(serializers.ModelSerializer):
    # it will dispaly all about songs field in one singer api, but we can only read it 
    # song = serializers.StringRelatedField(many=True,read_only=True)


    # HyperlinkedRelatedfield made link , in api if we click then we found particular song, but here view_name should child tablename then (-) then name
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')

    # and we have also slug field in that also slug_field should be our key (title)
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')

    # it return our child class that is song detail throught link ans our view-name = name-detail
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        # here song is not filed of singer but in foreign key we give song name so it display only id which is realted to singer song
        fields = ['id','name','gender','song']

