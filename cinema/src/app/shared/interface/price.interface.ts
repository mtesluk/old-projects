interface MovieAge {
    movie_3d: number;
    movie_2d: number;
}

export interface MoviePrice {
    adult: MovieAge;
    child: MovieAge;
}

interface SnackKind {
    popcorn: number;
    nachos: number;
    pepsi: number;
}

export interface SnackPrice {
    small: SnackKind;
    medium: SnackKind;
    large: SnackKind;
}

interface KitKind {
    popcorn_pepsi: number;
    nachos_pepsi: number;
}

export interface KitPrice {
    small: KitKind;
    medium: KitKind;
    large: KitKind;
}
