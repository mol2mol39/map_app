import type { GetServerSideProps, NextPage } from 'next'
import { useEffect, useState } from 'react'
import 'semantic-ui-css/semantic.min.css'
import { Loader } from 'semantic-ui-react'

interface SearchCatImage {
  id: string;
  url: string;
  width: number;
  height: number;
}

interface IndexPageProps {
  initialCatImageUrl: string;
}

const fetchCatImg = async (): Promise<SearchCatImage> => {
  const res = await fetch("https://api.thecatapi.com/v1/images/search");
  const result = await res.json();
  // console.log(result[0])
  return result[0];
}

// export async function getStaticProps() {
//   const { data } = await client.query({
//     query: gql`
//       query Countries {
//         countries {
//           code
//           name
//         }
//       }
//     `,
//   });
//   return {
//     props: {
//       countries: data.countries.slice(0, 4),
//     }
//   }
// }

// export interface CountriesData {
//   countries: Country[];
// }

const Home: NextPage<IndexPageProps> = ({ initialCatImageUrl }) => {
  const [catImgUrl, setCatImgUrl] = useState(initialCatImageUrl);
  const [isLoading, setIsLoading] = useState(false);
  
  const handleClick = async () => {
    setIsLoading(true);
    const catImage = await fetchCatImg();
    console.log(catImage);
    setCatImgUrl(catImage.url);
    setIsLoading(false);
  }
  return (
      <div style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh"
      }}>
          <h1>猫画像アプリ</h1>
          {isLoading ? (
            <Loader active size="huge" inline='centered' />
          ) : (
            <img src={catImgUrl} width={500} height="auto" />
          )}
          <button style={{ marginTop: 18 }} onClick={handleClick}>今日の猫さん</button>
      </div>
  )
}

export const getServerSideProps: GetServerSideProps<
  IndexPageProps
> = async () => {
  const catImage = await fetchCatImg();
  return {
    props: {
      initialCatImageUrl: catImage.url
    }
  }
};

export default Home
