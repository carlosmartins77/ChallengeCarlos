from sqlmodel import SQLModel, Field

class VideoBase(SQLModel):
    content_id: str = Field(unique=True)
    actual_label: str
    predicted_label: str
    feature_vector: str
    tvshow: str


class Video(VideoBase, table=True):
    id: int = Field(default=None, primary_key=True)  