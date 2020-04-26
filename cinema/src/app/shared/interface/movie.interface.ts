import { Time } from './time.interface';

export interface ImgMovie {
    url: string;
    caption?: string;
}

export interface Movie {
    en_movie_name: string;
    original_movie_name: string;
    times: Time[];
}
