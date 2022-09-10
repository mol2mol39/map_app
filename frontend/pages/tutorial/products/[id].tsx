import { useRouter } from "next/router";
import type { GetStaticProps, GetStaticPaths, NextPage } from 'next'
import Link from 'next/link';
import styles from "../../../styles/Home.module.css";
import { StringValueNode } from "graphql";

interface PathID {
  id: string;
}

interface ProductIF {
  id: string;
  name: string;
  image: string;
}

// SSGの場合
export const getStaticProps: GetStaticProps = async ({ params }) => {
  const req = await fetch(`http://localhost:3000/tutorial/${params.id}.json`);
  const data = await req.json();
  return {
    props: {
      product: data,
    }
  }
}

export const getStaticPaths: GetStaticPaths = async () => {
  const req = await fetch(`http://localhost:3000/tutorial/products.json`);
  const data = await req.json();
  const  paths = data.map((product: string) => {
    return {
      params: {
        id: product
      }
    }
  })
  return {
    paths,
    fallback: false
  }
}

// SSGの場合
// export async function getServerSideProps({ params }) {
//   const req = await fetch(`http://localhost:3000/tutorial/${params.id}.json`);
//   const data = await req.json();
//   return {
//     props: {
//       product: data,
//     }
//   }
// }

const Product: NextPage = ({ product }) => {
  const router = useRouter();
  const { id } = router.query;
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1>{id}のページです</h1>
        <img src={product.image} width="300" height="300" />
        <p>{product.name}</p>
        <br />
        <Link href="/tutorial/products">
          <a>商品一覧へ</a>
        </Link>
      </main>
    </div>
  );
}

export default Product;