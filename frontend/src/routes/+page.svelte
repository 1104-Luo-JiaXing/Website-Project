<script>
  import { PUBLIC_API_URL } from '$env/static/public';
  import { onMount } from 'svelte';

  let status = $state('checking...');

  onMount(async () => {
    const res = await fetch(`${PUBLIC_API_URL}/api/health`);
    const data = await res.json();
    status = data.status;
  });
</script>

<p>Backend says: {status}</p>