from typing import List, Literal
from pydantic import BaseModel, Field, HttpUrl

class Origin(BaseModel):
    name: str = Field(description="The name of the origin location.")
    url: str = Field(description="Link to the character's origin location.")

class CharacterLocation(BaseModel):
    name: str = Field(description="The name of the character's last known location endpoint.")
    url: str = Field(description="Link to the character's last known location endpoint.")

class Character(BaseModel):
    id: int = Field(description="The id of the character.")
    name: str = Field(description="The name of the character.")
    status: Literal['Alive', 'Dead', 'unknown'] = Field(description="The status of the character ('Alive', 'Dead' or 'unknown').")
    species: str = Field(description="The species of the character.")
    type: str = Field(description="The type or subspecies of the character.")
    gender: Literal['Female', 'Male', 'Genderless', 'unknown'] = Field(description="The gender of the character ('Female', 'Male', 'Genderless' or 'unknown').")
    origin: Origin = Field(description="Name and link to the character's origin location.")
    location: CharacterLocation = Field(description="Name and link to the character's last known location endpoint.")
    image: str = Field(description="Link to the character's image. All images are 300x300px and most are medium shots or portraits since they are intended to be used as avatars.")
    episode: List[str] = Field(description="List of episodes in which this character appeared.")
    url: str = Field(description="Link to the character's own URL endpoint.")
    created: str = Field(description="Time at which the character was created in the database.")

class Location(BaseModel):
    id: int = Field(description="The id of the location.")
    name: str = Field(description="The name of the location.")
    type: str = Field(description="The type of the location.")
    dimension: str = Field(description="The dimension in which the location is located.")
    residents: List[str] = Field(description="List of character who have been last seen in the location.")
    url: HttpUrl = Field(description="Link to the location's own endpoint.")
    created: str = Field(description="Time at which the location was created in the database.")

class Episode(BaseModel):
    id: int = Field(description="The id of the episode.")
    name: str = Field(description="The name of the episode.")
    air_date: str = Field(description="The air date of the episode.")
    episode: str = Field(description="The code of the episode.")
    characters: List[str] = Field(description="List of characters who have been seen in the episode.")
    url: str = Field(description="Link to the episode's own endpoint.")
    created: str = Field(description="Time at which the episode was created in the database.")
