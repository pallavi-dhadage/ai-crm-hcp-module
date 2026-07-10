export class AgentService {
  private eventSource: EventSource | null = null;

  stream(
    message: string,
    onChunk: (chunk: string) => void,
    onComplete: () => void,
    onError: (error: Error) => void
  ) {
    const url = `http://localhost:8000/api/agent/stream?message=${encodeURIComponent(message)}`;
    this.eventSource = new EventSource(url);

    this.eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'chunk') {
        onChunk(data.content);
      } else if (data.type === 'complete') {
        onComplete();
        this.eventSource?.close();
      } else if (data.type === 'error') {
        onError(new Error(data.content));
        this.eventSource?.close();
      }
    };

    this.eventSource.onerror = () => {
      onError(new Error('Connection lost'));
      this.eventSource?.close();
    };
  }

  disconnect() {
    this.eventSource?.close();
    this.eventSource = null;
  }
}
